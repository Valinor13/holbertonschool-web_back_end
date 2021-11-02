#!/usr/bin/env python3
""" This module contains type annotated functions """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:

    """ To KV: Creates a tuple
            Params:
                k: string - first value in tuple
                v: int/float - base for second value in tuple
            Variables:
                sq: float - square of v
            Return:
                Tuple with first value k and second value sq """

    sq: float = (v * v)

    return (k, sq)
