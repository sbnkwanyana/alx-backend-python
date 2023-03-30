#!/usr/bin/env python3
"""
Module contains function floor that returns the floor of a float
"""


def floor(n: float) -> int:
    """
    floor() -> int: type-annotated function takes float (n)
    and returns a the floor value (int).
    """
    return n.__floor__()
