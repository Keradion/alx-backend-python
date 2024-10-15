#!/usr/bin/env python3
"""
   Write an asynchronous coroutine that takes in an integer argument
   (max_delay, with a default value of 10) named wait_random that wait
   for a random delay between 0 and max_delay (included and float value)
   seconds and eventually returns it.
   Use the random module.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """generate a random float value and pause for a duration
       equivalent to the value and returns it.
    """
    random_delay = random.uniform(0, max_delay)  # Generate random float value
    await asyncio.sleep(random_delay)  # pause for a duration of random delay

    return random_delay
