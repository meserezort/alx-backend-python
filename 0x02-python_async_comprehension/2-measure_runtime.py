#!/usr/bin/env python3
"""
    Measure runtime function
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    will execute async_comprehension four times in parallel
    using asyncio.gather, then return the total execution time

    Return:
    float - total execution time
    """
    start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension()
                         )
    end = time.time()
    return (end - start)
