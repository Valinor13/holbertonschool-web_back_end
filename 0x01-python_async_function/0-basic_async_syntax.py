#!/usr/bin/env python3
""" This module contains async/await functions """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:

    """ Wait Random: Waits a random amount of time between 0 - 10 seconds
            Params:
                max_delay: int - An integer representing the max delay time
            Variables:
                time: float - Float value assigned by random call
            Return:
                Float value of the actual time spent waiting """

    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
