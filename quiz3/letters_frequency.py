"""
Student ID: 109704065
Credit by K.Wei
"""
import numpy as np

def get_freq(str):
    """
    input discription
    @str: the string or list you want to get its frequency for every alphabet
    """
    freq = {}
    for letter in str:
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter] += 1
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    return sorted_freq