#!/usr/bin/env python3
'''Task 7 answer
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is the string k and the second element
    is the square of the int or float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing string k and the square of v as a float.
    """
    return (k, float(v) ** 2)

