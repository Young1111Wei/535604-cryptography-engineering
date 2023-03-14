import letters_frequency
import formula
import group as get_group
import sys

# constants
ROUND = 10
TARGET_IC = 0.068 # English
EPSILON = 0.005

# message stdin
mes = input()

# remove space
mes = mes.replace(' ', '')

# initialize to store the target value
min_key_length = 0
target_groups = []
size = len(mes)
key = []
record_j = 0
plaintext = ['\0'] * size
freq_eng = letters_frequency.get_english_frequency()
for alphabet, frequency in freq_eng.items():
    freq_eng[alphabet] = frequency/100

# find the key length
for key_length in range(1, ROUND+1):
    # initialize the 2D list to store alphabets from every group
    groups = get_group.get_groups(mes, key_length)

    # initialize ic for every group
    groups_ic = [0 for _ in range(key_length)]

    # get ic of every group
    for i, group in enumerate(groups):
        freq = letters_frequency.get_freq(group)
        ic = formula.get_ic(group, freq)
        groups_ic[i] = ic

    # get avg ic from all groups and difference between avg ic and target ic
    avg = sum(groups_ic) / len(groups_ic)
    differ = abs(avg - TARGET_IC)
    
    # compare if the avg ic is "close" to the value of target ic
    if differ < EPSILON:
        # print the avg ic
        #print("key_length:", key_length)
        #print("average ic:", avg)
        min_key_length = key_length
        target_groups = groups
        break

for i, group in enumerate(target_groups):
    # initialize variables
    min_chi = sys.maxsize
    shift_n = 0
    
    # find the smallist chi-square
    for j in range(26):
        shifted_list = formula.shift_alphabet(group, -j)
        freq = letters_frequency.get_freq(shifted_list)
        for alphabet, frequency in freq.items():
            freq[alphabet] = frequency/len(shifted_list)
        chi = formula.get_cai_square(freq, freq_eng)
        if min_chi > chi:
            min_chi = chi
            record_j = -j
    # store the key for this group
    key.append(chr(-record_j+65))
    target_groups[i] = formula.shift_alphabet(target_groups[i], record_j)

# combine groups to plain text
plaintext = formula.combine_group(target_groups, size)

# stdout to file
filename = 'message2_out.txt'
file = sys.stdout
sys.stdout = open(filename, 'w')

# print the plain text to file with stdout
for index, alphabet in enumerate(plaintext):
#    if index!=0 and index%min_key_length == 0:
#        sys.stdout.write(' ')
    sys.stdout.write(alphabet)
sys.stdout.write("\n")

# close file
sys.stdout.close()
sys.stdout = file

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
for every group:
    get this group frequency
    get the highest freq
    get E and highest freq alphabet distance
    translate every alphabet
"""