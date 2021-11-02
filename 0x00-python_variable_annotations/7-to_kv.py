#!/usr/bin/env python3
""" This module contains type annotated functions """


from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple:

    """ To KV: Creates a tuple
            Params:
                k: string - first value in tuple
                v: int/float - base for second value in tuple
            Variables:
                sqRt: float - square root of v
            Return:
                Tuple with first value k and second value sqRt """

    sqRt: float = math.sqrt(v)

    return (k, sqRt)
