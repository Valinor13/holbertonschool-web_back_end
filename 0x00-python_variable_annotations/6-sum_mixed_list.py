#!/usr/bin/env python3
""" This module contains type annotated functions """


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:

    """ Sum Mixed List: Adds list of floats & ints to sum
            Params:
                mxd_list: List[float, int] - List of float or int values
            Variables:
                sum: float - running total of all list values
            Return:
                Sum of all values in input_list """

    sum: float = 0.0

    for value in mxd_list:
        sum = sum + value

    return sum
