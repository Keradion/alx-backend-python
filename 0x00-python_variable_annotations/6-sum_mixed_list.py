#!/usr/bin/env python3
"""
   Write a type-annotated function sum_mixed_list which takes
   a list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
       takes a List of int and floats as arguments and
       returns their sum as a float.
    """
    return sum(mxd_lst)
