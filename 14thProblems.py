# Multiples of 3 or 5
def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

# Mexican Wave
def wave(people):
    return [people[:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if people[i].isalpha() and people[i].islower()]

# Count characters in your string
def count(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    return char_count