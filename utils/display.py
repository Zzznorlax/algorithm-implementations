

from typing import Any, List


DEFAULT_BRACKET_FORMAT = "[{}]"


def format_list(array: List[Any], spacing: int = 3, separater: str = ", ", bracket_format: str = DEFAULT_BRACKET_FORMAT) -> str:
    return DEFAULT_BRACKET_FORMAT.format(separater.join([str(element).rjust(spacing) for element in array]))
