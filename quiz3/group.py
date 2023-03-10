"""
Student ID: 109704065
Credit by K.Wei
"""

def get_groups(message, key_length):
    """
    input
        @message: the string you want to break to every group
        @key_length: the number of group
    output
        @groups: a 2D list
    """
    # initialize the 2D list to store alphabets from every group
    groups = [[] for _ in range(key_length)]

    # group the input message by @key_length
    for i, letter in enumerate(message):
        groups[i%key_length].append(letter)
    
    return groups