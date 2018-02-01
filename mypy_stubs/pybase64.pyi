from typing import Optional


def b64encode(s: bytes, altchars: Optional[bytes] = None) -> bytes:
    ...


def b64decode(s: bytes, altchars: Optional[bytes] = None, validate: bool = False) -> bytes:
    ...


def standard_b64encode(s: bytes) -> bytes:
    ...


def standard_b64decode(s: bytes) -> bytes:
    ...


def urlsafe_b64encode(s: bytes) -> bytes:
    ...


def urlsafe_b64decode(s: bytes) -> bytes:
    ...


def get_version() -> str:
    ...


def get_license_text() -> str:
    ...
