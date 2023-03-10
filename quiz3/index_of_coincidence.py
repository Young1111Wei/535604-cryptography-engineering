"""
Student ID: 109704065
Credit by K.Wei
"""
import numpy as np

def get_ic(str, freq):
    """
    input
        @str: the string or list you want to be calculated
        @freq: the frequency of every alphabet in your str
    output
        return the index of coincidence
    """
    sum = 0 # sum of the series
    for f in freq:
        sum += freq[f] * (freq[f]-1)

    size = len(str)

    return (sum / (size*(size-1))) # definition of index of coincidence