#!/usr/bin/env python3
""" This module contains async/await functions """


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:

    """ Async Comprehension: Calls async_generator. Appends the yields to list
            Variables:
                result: list - list of float values interpreted from yields
            Return:
                A list of yields converted to their float results """

    result = []
    async for i in async_generator():
        result.append(i)
    return result
