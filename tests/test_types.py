"""Test types with mypy.

Do not use any site-packages packages/modules here except the `nsjwt`
"""

import collections
from typing import Any, Hashable, Generator

import nsjwt


def test_decode_token_types() -> None:
    token_bytes = (
        b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJKYW1'
        b'lcyBCbGFja3NoYXciLCJhZG1pbiI6dHJ1ZX0.gBX27BCOBuYNZP3m42Xd9plBlylfcVr'
        b'Q72OcsEY_1Ao'
    )
    token_str = (
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJKYW1l'
        'cyBCbGFja3NoYXciLCJhZG1pbiI6dHJ1ZX0.gBX27BCOBuYNZP3m42Xd9plBlylfcVrQ7'
        '2OcsEY_1Ao'
    )
    token_bytearray = bytearray(
        b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJKYW1'
        b'lcyBCbGFja3NoYXciLCJhZG1pbiI6dHJ1ZX0.gBX27BCOBuYNZP3m42Xd9plBlylfcVr'
        b'Q72OcsEY_1Ao'
    )
    secret = 'secret'
    nsjwt.decode(secret, token_bytes)
    nsjwt.decode(secret, token_str)
    nsjwt.decode(secret, token_bytearray)


def test_decode_secret_types() -> None:
    token = (
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJKYW1l'
        'cyBCbGFja3NoYXciLCJhZG1pbiI6dHJ1ZX0.gBX27BCOBuYNZP3m42Xd9plBlylfcVrQ7'
        '2OcsEY_1Ao'
    )
    nsjwt.decode(b'secret', token)
    nsjwt.decode('secret', token)
    nsjwt.decode(bytearray(b'secret'), token)


def test_encode_secret_types() -> None:
    nsjwt.encode(b'secret', {})
    nsjwt.encode('secret', {})
    nsjwt.encode(bytearray(b'secret'), {})


class MyMapping(collections.Mapping):
    def __getitem__(self, key: Hashable) -> Any:
        return 'value'

    def __iter__(self) -> Generator:
        yield from ['key']

    def __len__(self) -> int:
        return 1


def test_encode_payload_types() -> None:
    nsjwt.encode('secret', {})
    nsjwt.encode('secret', MyMapping())
