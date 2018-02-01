"""Unit tests for nsjwt
"""

import nsjwt


def test_encode_and_decode():
    """Test decode encoded value."""
    secret = 'секрет'
    payload = {'sub': '42', 'name': 'Азат Курбанов', 'admin': True}
    assert nsjwt.decode(secret, nsjwt.encode(secret, payload)) == payload


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
