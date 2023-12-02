# Unique In Order
def unique_in_order(sequence):
    letters = []
    
    for i in range(len(sequence)):
        if (i == 0) or (sequence[i] != sequence[i - 1]):
            letters.append(sequence[i])
            
    return letters

# Find the unique number
def find_uniq(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

# Replace With Alphabet Position
def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    return " ".join([str(alphabet.find(alph) + 1) for alph in text.lower() if alph in alphabet])