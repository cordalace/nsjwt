"""This module contains set of exceptions for nsjwt."""

class BaseTokenException(Exception):
    """Base JWT exception."""


class ExpectedMappingError(BaseTokenException):
    """Instance of collections.abc.Mapping expected as payload."""


class SignatureDoesntMatchError(BaseTokenException):
    """Payload signature and calculated signature not same."""


class NotDictInstanceError(BaseTokenException):
    """Expected an instance of dict as payload"""


class TokenRegexpDoesntMatchError(BaseTokenException):
    """Regexp of JWT doesn't match on received token"""
