import letters_frequency
import index_of_coincidence

# message stdin
mes = input("Enter message: ")
print() # change line in output

# get the max groups number user want to test
max = int(input("Enter max number of groups you want to calculate ICs: "))
print() # change line in output

# remove space
mes = mes.replace(' ', '')

for key_length in range(1,max+1):
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

    # get avg ic of all groups
    avg = sum(groups_ic) / len(groups_ic)
    print(key_length, " groups of average IC is: ", avg)
    
""" draft
get input
filter str
sperate to different groups
calculate ic from every group
avarage total ic
"""