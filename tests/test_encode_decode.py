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

"""Unit tests for nsjwt."""

import pytest

import nsjwt


@pytest.mark.parametrize('token', [
    # bytes
    (
        b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJKYW1'
        b'lcyBCbGFja3NoYXciLCJhZG1pbiI6dHJ1ZX0.gBX27BCOBuYNZP3m42Xd9plBlylfcVr'
        b'Q72OcsEY_1Ao'
    ),
    # str
    (
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJKYW1l'
        'cyBCbGFja3NoYXciLCJhZG1pbiI6dHJ1ZX0.gBX27BCOBuYNZP3m42Xd9plBlylfcVrQ7'
        '2OcsEY_1Ao'
    ),
    # bytearray
    bytearray(
        b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJKYW1'
        b'lcyBCbGFja3NoYXciLCJhZG1pbiI6dHJ1ZX0.gBX27BCOBuYNZP3m42Xd9plBlylfcVr'
        b'Q72OcsEY_1Ao'
    ),
])
def test_decode_token_types(token):
    """Test decode with different types of `token` parameter."""
    secret = 'secret'
    payload = {'sub': '42', 'name': 'James Blackshaw', 'admin': True}
    assert nsjwt.decode(secret, token) == payload


@pytest.mark.parametrize('secret', [
    b'secret',  # bytes
    'secret',  # str
    bytearray(b'secret'),  # bytearray
    'секрет'.encode(),  # bytes
    'секрет',  # str
    bytearray('секрет'.encode()),  # bytearray
])
def test_secret_types(secret):
    """Test encode/decode with different types of `secret` parameter."""
    payload = {'sub': '42', 'name': 'Джон Фэи', 'admin': True}
    token = nsjwt.encode(secret, payload)
    assert nsjwt.decode(secret, token) == payload


def test_encode_invalid_payload():
    """Test encode with invalid signature type."""
    secret = 'secret'
    payload = 'not-mapping-payload'
    with pytest.raises(nsjwt.ExpectedMappingError) as exc_info:
        nsjwt.encode(secret, payload)
    assert str(exc_info.value) == (
        'Invalid payload, expected Mapping: not-mapping-payload'
    )
    assert exc_info.type == nsjwt.ExpectedMappingError


def test_decode_invalid_sig():
    """Test decode with unexpected signature type."""
    secret_encode = 'secret-encode'
    secret_decode = 'secret-decode'
    payload = {'sub': '42', 'name': 'Glenn Jones', 'admin': True}
    with pytest.raises(nsjwt.SignatureMismatchError) as exc_info:
        nsjwt.decode(secret_decode, nsjwt.encode(secret_encode, payload))
    assert str(exc_info.value) == "Invalid signature"
    assert exc_info.type == nsjwt.SignatureMismatchError


def test_decode_invalid_payload():
    """Test decode with invalid signature."""
    secret = 'secret'
    # payload = 'non-json-object-payload'
    token = (
        b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.Im5vbi1qc29uLW9iamVjdC1wYXlsb2F'
        b'kIg.bX0x3jquACcA9WUM5lxvJkXToSETeF9il7h-GckygxM'
    )
    with pytest.raises(nsjwt.NotDictInstanceError) as exc_info:
        nsjwt.decode(secret, token)
    assert str(exc_info.value) == 'Invalid payload: non-json-object-payload'
    assert exc_info.type == nsjwt.NotDictInstanceError


def test_decode_invalid_token():
    """Test decode with invalid token."""
    secret = 'secret'
    token = (
        b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.foobar'
    )
    with pytest.raises(nsjwt.TokenInvalidError) as exc_info:
        nsjwt.decode(secret, token)
    assert str(exc_info.value) == 'Invalid token'
    assert exc_info.type == nsjwt.TokenInvalidError


def test_invalid_token_payload():
    """Test decode invalid token with payload."""
    secret = 'secret'
    token = (
        b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.foobar.spam'
    )
    with pytest.raises(nsjwt.TokenInvalidError) as exc_info:
        nsjwt.decode(secret, token)
    assert str(exc_info.value) == 'Invalid payload'
    assert exc_info.type == nsjwt.TokenInvalidError


def test_decode_jwt_io():
    """Try to decode token copypasted from https://jwt.io."""
    secret = 'секрет'
    payload = {'sub': '42', 'name': 'Азат Курбанов', 'admin': True}
    # token from jwt.io
    token = (
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiLQkNC3'
        '0LDRgiDQmtGD0YDQsdCw0L3QvtCyIiwiYWRtaW4iOnRydWV9.0WbG6yjgXT9XgALPdJlS'
        'dXkfiL8_ik2JBDgncdlRosU'
    )
    assert nsjwt.decode(secret, token) == payload
