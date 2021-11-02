#!/usr/bin/env python3
""" This module contains type annotated functions """


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """ Element Length: Creates a tuple of iterable and it's length
            Params:
                lst: Iterable - iterable of sequence objects
            Return:
                Tuple with sequence & sequence length """

    return [(i, len(i)) for i in lst]
