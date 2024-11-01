"""Default functions to set up priority rules for the Priority Queue."""
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def reverse(x: Any) -> Any:
    """Priority function for max heap behavior."""
    return -x


def by_length(x: Any) -> int:
    """Priority function using length of items."""
    return len(x)


def by_attr(attr_name: str) -> Callable[[Any], Any]:
    """Create a priority function using an attribute of items."""

    def priority_func(x: Any) -> Any:
        return getattr(x, attr_name)

    return priority_func
