"""
Student ID: 109704065
Credit by K.Wei
"""
import numpy as np
import math 

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

def get_cai_square(freq, freq_eng):
    """
    input
        @freq: a list of frequency
        @freq_eng: a list of frequency of english
    output
        return the x of chi-square test
    """
    sum = 0
    for alphabet in range(26):
        i = chr(alphabet+65)
        if i in freq:
            observed = freq[i]
        else:
            observed = 0
        expected = freq_eng[i]
        # print("i: ", i, ", observed: ", observed, ", expected: ", expected)
        sum = sum + (((observed - expected)**2)/expected)
    return sum

def shift_alphabet(list, n):
    """
    input
        @list: alphabet list
        @n: shift number of position
    output
        return the the result
    """
    ret_list = ['\0'] * len(list)
    for i, alphabet in enumerate(list):
        ret_list[i] = chr(((ord(alphabet) - 65) + n)%26 + 65)
    return ret_list

def combine_group(groups, length):
    combined = ['\0'] * length
    key_length = len(groups)
    for i, group in enumerate(groups):
        for j, alphabet in enumerate(group):
            combined[j*key_length+i] = alphabet
    return combined