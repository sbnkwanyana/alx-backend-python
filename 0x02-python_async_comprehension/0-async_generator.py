#!/usr/bin/env python3
"""
Module contains function async_generator that yield returns to random values
"""
import asyncio
import random


async def async_generator() -> float:
    """
    function yield returns 10 random values after sleeping for 1 second
    between each return
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
