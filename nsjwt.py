# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""nsjwt - no shit jwt implementation."""

import re
import hashlib
import hmac
from typing import Mapping, Union

import pybase64
import ujson

__all__ = ['encode', 'decode']

HEADER_SEGMENT_DOTTED = b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
TOKEN_RE = re.compile(r'[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]')


def _base64_url_encode(data: bytes) -> bytes:
    return pybase64.urlsafe_b64encode(data).replace(b'=', b'')


def _base64_url_decode(data: bytes) -> bytes:
    # See: https://stackoverflow.com/a/9807138
    padding_len = len(data) % 4
    if padding_len:
        data += b'=' * (4 - padding_len)
    return pybase64.urlsafe_b64decode(data)


def encode(secret: Union[str, bytes], payload: Mapping) -> bytes:
    """Encode JWT."""
    if isinstance(secret, str):
        secret = secret.encode()
    payload_json = ujson.dumps(payload, ensure_ascii=False).encode()
    payload_segment = _base64_url_encode(payload_json)
    signing_input = HEADER_SEGMENT_DOTTED + payload_segment
    signature = hmac.new(secret, signing_input, hashlib.sha256).digest()
    signature_segment = _base64_url_encode(signature)
    return signing_input + b'.' + signature_segment


def decode(secret: Union[str, bytes], token: Union[str, bytes]) -> Mapping:
    """Decode JWT."""
    if isinstance(secret, str):
        secret = secret.encode()
    if isinstance(token, str):
        token = token.encode()
    signing_input, signature_segment = token.rsplit(b'.', 1)
    payload_segment = signing_input.split(b'.', 1)[1]
    payload = ujson.loads(_base64_url_decode(payload_segment).decode())
    signature = _base64_url_decode(signature_segment)
    calculated_signatue = hmac.new(secret, signing_input,
                                   hashlib.sha256).digest()
    if not hmac.compare_digest(signature, calculated_signatue):
        raise RuntimeError('Invalid signature')
    return payload


def prevalidate(token: Union[str, bytes]) -> None:
    """Prevalidate JWT."""
    if isinstance(token, bytes):
        token = token.decode()
    if TOKEN_RE.match(token) is None:
        raise RuntimeError('Invalid token')


def test():
    """Tests1."""
    secret = 'секрет'
    payload = {'sub': '42', 'name': 'Азат Курбанов', 'admin': True}
    assert decode(secret, encode(secret, payload)) == payload
    # token from jwt.io
    token = (
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiLQkNC3'
        '0LDRgiDQmtGD0YDQsdCw0L3QvtCyIiwiYWRtaW4iOnRydWV9.0WbG6yjgXT9XgALPdJlS'
        'dXkfiL8_ik2JBDgncdlRosU'
    )
    assert decode(secret, token) == payload


if __name__ == '__main__':
    test()
