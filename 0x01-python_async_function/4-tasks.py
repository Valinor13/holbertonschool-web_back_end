#!/usr/bin/env python3
""" This module contains async/await functions """


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:

    """ Task Wait N: Calls the task wait random function n times
            Params:
                n: int - An integer indicating how many times to call the
                         wait_random function
                max_delay: int - An integer representing the max delay time
            Variables:
                time_list: List[future] - List of futures assigned by
                                          random call
                time_list_ascending: List[float] - List of floats returned by
                                                   futures
            Return:
                Time list in ascending order """

    time_list = []
    time_list_ascending = []

    for i in range(n):
        time_list.append(task_wait_random(max_delay))

    for future in asyncio.as_completed(time_list):
        time_list_ascending.append(await future)

    return time_list_ascending
