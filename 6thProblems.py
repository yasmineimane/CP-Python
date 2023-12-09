# Duplicate Encoder
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(i) == 1 else ")" for i in word.lower()])

# Take a Ten Minutes Walk
def is_valid_walk(walk):
    countSN = walk.count('s') == walk.count('n')
    countWE = walk.count('w') == walk.count('e')
    length = len(walk) == 10
    
    return countSN and countWE and length


# Detect Pangram
def is_pangram(s):
    alphabit = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in alphabit:
        if letter not in s.lower():
            return False
    return True

# Sort the odd
def sort_array(source_array):

    oddSortedArray = sorted([x for x in source_array if x%2 != 0])
    n = 0

    for i, e in enumerate(source_array):
        if e%2 !=0:
            source_array[i] = oddSortedArray[n]
            n += 1
            
    return source_array

# Moving Zeros To The End
def move_zeros(lst):
    count = 0
    i = 0
    
    while 0 in lst:
        lst.remove(0)
        count += 1
    
    while i < count:
        lst.append(0)
        i += 1
        
    return lst