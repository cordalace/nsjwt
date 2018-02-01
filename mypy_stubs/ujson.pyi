from typing import Any, Text, Union


def dumps(obj: Any,
    ensure_ascii: bool = ...,
    encode_html_chars: bool = ...,
    double_precision: int = ...,
    escape_forward_slashes: bool = ...,
    indent: int = ...) -> str: ...


def loads(s: Union[Text, bytes],
    precise_float: bool = ...) -> Any: ...
