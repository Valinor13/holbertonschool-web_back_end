#!/usr/bin/env python3
""" This module contains async/await functions """


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:

    """ Async Comprehension: Calls async_generator. Appends the yields to list
            Return:
                A list of yields converted to their float results """

    return [i async for i in async_generator()]
