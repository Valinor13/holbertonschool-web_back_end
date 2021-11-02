#!/usr/bin/env python3
""" This module contains type annotated functions """


from typing import List


def sum_list(input_list: List[float]) -> float:

    """ Sum List: Adds list of floats to sum
            Params:
                input_list: list[float] - List of float values
            Variables:
                sum: float - running total of float values
            Return:
                Sum of all float values in input_list """

    sum: float = 0.0

    for value in input_list:
        sum = sum + value

    return sum
