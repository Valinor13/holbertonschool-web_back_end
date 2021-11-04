#!/usr/bin/env python3
""" This module contains async/await functions """


import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:

    """ Measure Runtime: Calls async_comprehension 4 times in parallel
            Variables:
                start: float - Start time of operation
                finish: float - finish time of operation
            Return:
                Float representing the total runtime of the op in seconds """

    start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    finish = time.time()
    return (finish - start)
