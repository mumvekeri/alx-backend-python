#!/usr/bin/env python3
''' task 9 answer
'''
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Return a list of tuples where each tuple contains an element from the input list `lst`
    along with its length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains an element
                               from `lst` and its corresponding length.
    """
    return [(i, len(i)) for i in lst]

