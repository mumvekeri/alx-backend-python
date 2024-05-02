#!/usr/bin/env python3
'''Task 9 answer
'''
from typing import Iterable, List, Tuple, Union


def element_length(lst: Iterable[Union[str, bytes]]) -> List[Tuple[Union[str, bytes], int]]:
    '''
    Generate a list of tuples where each tuple contains an element from the input iterable `lst`
    along with its length.

    Args:
        lst (Iterable[Union[str, bytes]]): An iterable of strings or bytes.

    Returns:
        List[Tuple[Union[str, bytes], int]]: A list of tuples where each tuple contains an element
                                              from `lst` and its corresponding length.
    '''
    return [(i, len(i)) for i in lst]
