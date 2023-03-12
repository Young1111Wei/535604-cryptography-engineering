import letters_frequency
import formula
import sys

mes = input()
min_chi = sys.maxsize
key = '\0'
freq_eng = letters_frequency.get_english_frequency()
for alphabet, frequency in freq_eng.items():
    freq_eng[alphabet] = frequency/100

group = []
for a in mes:
    group.append(a)

for i in range(26):
    print("group: ", group)
    print("Round: ", chr(i+65))
    shifted = formula.shift_alphabet(group, -i)
    print("Message: ", end='')
    for a in shifted:
        print(a, end='')
    print()
    
    freq = letters_frequency.get_freq(shifted)
    for alphabet, frequency in freq.items():
        freq[alphabet] = frequency/len(shifted)
    print("Frequency: ", freq)
    
    chi = formula.get_cai_square(freq, freq_eng)
    print("chi: ", chi)
    print()
    if min_chi > chi:
        min_chi = chi
        key = chr(i+65)

print("key: ", key)

for i in range(25, -1, -1):
    print(i, end=', ')