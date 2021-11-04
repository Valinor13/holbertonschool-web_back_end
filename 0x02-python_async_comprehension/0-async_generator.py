#!/usr/bin/env python3
""" This module contains async/await functions """


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:

    """ Async Generator: Loops 10 times each time creating a new operation
                         that sleeps for 1 second and then yields a random
                         float number between 0 and 10
            Return:
                There is no function return. The future yields results """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
