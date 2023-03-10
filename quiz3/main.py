import letters_frequency
import index_of_coincidence
import group

# constants
ROUND = 10
TARGET_IC = 0.068 # English
EPSILON = 0.005

# message stdin
mes = input("Enter message: ")
print() # change line in output

# remove space
mes = mes.replace(' ', '')

min_key_length = 0
for key_length in range(1, ROUND+1):
    # initialize the 2D list to store alphabets from every group
    groups = [[] for _ in range(key_length)]

    # group the input message by @key_length
    for i, letter in enumerate(mes):
        groups[i%key_length].append(letter)

    # initialize ic for every group
    groups_ic = [0 for _ in range(key_length)]

    # get ic of every group
    for i, group in enumerate(groups):
        freq = letters_frequency.get_freq(group)
        ic = index_of_coincidence.get_ic(group, freq)
        groups_ic[i] = ic

    # get avg ic from all groups and difference between avg ic and target ic
    avg = sum(groups_ic) / len(groups_ic)
    differ = abs(avg - TARGET_IC)
    
    # print the avg ic
    print("key_length: ", key_length, ", average ic: ", avg)
    
    # compare if the avg ic is "close" to the value of target ic
    if differ < EPSILON:
        min_key_length = key_length
        break


    
""" draft
get input
filter str
for every key length in MAX_ROUND:
    sperate to different groups
    calculate ic from every group
    avarage total ic
    differ = abs(avg_ic - TARGET_IC)
    if differ < EPSILON:
        record key_length
        break
"""