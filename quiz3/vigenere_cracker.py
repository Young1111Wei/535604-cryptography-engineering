import letters_frequency
import formula
import group as get_group
import sys

class Cracker:    
    def __init__(self, message, round, target_ic, epsilon):
        # initialize the config variables
        self.message = message
        self.round = round
        self.target_ic = target_ic
        self.epsilon = epsilon
        
        # initialize to store the target value
        self.min_key_length = 0
        self.target_groups = []
        self.size = len(self.message)
        self.key = []
        self.record_j = 0
        self.plaintext = ['\0'] * self.size
        self.freq_eng = letters_frequency.get_english_frequency()
        for alphabet, frequency in self.freq_eng.items():
            self.freq_eng[alphabet] = frequency/100
            
    def get_key_length(self):
        # find the key length
        for key_length in range(1, self.round+1):
            # initialize the 2D list to store alphabets from every group
            groups = self.get_groups(self.message, key_length)

            # initialize ic for every group
            groups_ic = [0 for _ in range(key_length)]

            # get ic of every group
            for i, group in enumerate(groups):
                freq = letters_frequency.get_freq(group)
                ic = formula.get_ic(group, freq)
                groups_ic[i] = ic

            # get avg ic from all groups and difference between avg ic and target ic
            avg = sum(groups_ic) / len(groups_ic)
            differ = abs(avg - self.target_ic)
            
            # compare if the avg ic is "close" to the value of target ic
            if differ < self.epsilon:
                # print the avg ic
                print("key_length:", key_length)
                print("average ic:", avg)
                min_key_length = key_length
                target_groups = groups
                break
    
    def get_groups(self, key_length):
        """
        input
            @key_length: the number of group
        output
            @groups: a 2D list
        """
        # initialize the 2D list to store alphabets from every group
        groups = [[] for _ in range(key_length)]

        # group the input message by @key_length
        for i, letter in enumerate(self.message):
            groups[i%key_length].append(letter)
        
        return groups

    def get_freq(self):
        """
        output
            @sorted_freq: a sorted list which record the frequency for every alphabet
        """
        freq = {}
        for letter in self.message:
            if letter not in freq:
                freq[letter] = 1
            else:
                freq[letter] += 1
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        return sorted_freq
            
    def get_english_frequency():
        letter_frequency = {'E' : 12.0,
            'T' : 9.10,
            'A' : 8.12,
            'O' : 7.68,
            'I' : 7.31,
            'N' : 6.95,
            'S' : 6.28,
            'R' : 6.02,
            'H' : 5.92,
            'D' : 4.32,
            'L' : 3.98,
            'U' : 2.88,
            'C' : 2.71,
            'M' : 2.61,
            'F' : 2.30,
            'Y' : 2.11,
            'W' : 2.09,
            'G' : 2.03,
            'P' : 1.82,
            'B' : 1.49,
            'V' : 1.11,
            'K' : 0.69,
            'X' : 0.17,
            'Q' : 0.11,
            'J' : 0.10,
            'Z' : 0.07 }
        return letter_frequency
    