#!/usr/bin/env python3
'''Task 9 answer
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Let's duck type an iterable object
    '''
    return [(i, len(i)) for i in lst]

