#!/usr/bin/env python3
""" This module contains async/await functions """


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:

    """ Task Wait Random: Calls the wait_random function using max_delay
            Params:
                max_delay: int - An integer representing the max delay time
            Return:
                The future returned by creating the task """

    return asyncio.create_task(wait_random(max_delay))
