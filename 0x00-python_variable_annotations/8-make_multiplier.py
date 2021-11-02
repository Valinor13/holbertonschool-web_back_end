#!/usr/bin/env python3
""" This module contains type annotated functions """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """ Make Multiplier: Create a mulitplier function
            Params:
                mulitplier: float - number to multiply by with function
            Callbacks:
                multiplyBy: function - takes mulitplier and uses it to
                                       multiply against input
            Return:
                Callback function mulitplyBy """

    def multiplyBy(num: float) -> float:

        """ Multiply By: Multiplies a number by the multiplier
            Params:
                num: float - number to be multiplied
            Return:
                num * multiplier """

        return (multiplier * num)

    return multiplyBy
