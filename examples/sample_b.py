
"""
Sample B module.

This module contains utility functions for generating sequences
and processing numbers.
"""

def generator_example(n):
    """
    Generate a sequence of numbers up to n.
    
    Parameters
    ----------
    n : TYPE
        Upper limit of the sequence
    """
    for i in range(n):
        yield i


def raises_example(x):
    """
    Raise ValueError for negative input.
    
    Parameters
    ----------
    x : TYPE
        Input value
    
    Raises
    ------
    ValueError
        Value is negative.
    """
    if x < 0:
        raise ValueError("negative")
    return x * 2
