#!/usr/bin/env python3
"""function with integers n and
max_delay as arguments that measures
the total execution time for wait_n(n,
max_delay), and returns total_time / n
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random that takes an
    integer max_delay and returns a asyncio.Task.
    """

    return asyncio.create_task(wait_random(max_delay))
