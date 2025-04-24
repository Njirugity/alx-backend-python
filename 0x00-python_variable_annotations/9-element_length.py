#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
"""
type-annotated function
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst- a sequence
    Returns:
        the items"""
    return [(i, len(i)) for i in lst]
