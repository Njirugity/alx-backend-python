#!/usr/bin/env python3
from typing import Union, Tuple
"""
type-annotated function to_kv that
takes a string k and an int OR float v
as arguments and returns a tuple.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k- a string
        v- an int or a float
    Return:
        a tuple with the string k and
        the square of v
    """
    return (k, v**2)
