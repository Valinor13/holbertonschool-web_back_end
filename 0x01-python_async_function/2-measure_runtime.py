#!/usr/bin/env python3
""" This module contains async/await functions """


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:

    """ Measure Time: Measures the runtime of the created async functions
            Params:
                n: int - An integer indicating how many times to call the
                         wait_random function
                max_delay: int - An integer representing the max delay time
            Variables:
                start: float - Timestamp of the start of function calls
                finish: float - Timestamp of the finish of function calls
            Return:
                Runtime in seconds of async functions """

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    finish = time.time()
    return (finish - start)
