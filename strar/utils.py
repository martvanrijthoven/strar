import re
from typing import Any, Callable, Tuple


class Text:
    BOLD = "\033[1m"
    BOLD_END = "\033[0m"

    @staticmethod
    def lower(text: str) -> str:
        return text.lower()

    @staticmethod
    def split_capitals_with_underscore(text: str) -> str:
        return "_".join(re.findall(".[^A-Z]*", text))


def chain_functions(x: Any, *functions: Tuple[Callable]) -> Any:
    for function in functions:
        x = function(x)
    return x
