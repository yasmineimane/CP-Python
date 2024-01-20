# Watermelon
def watermelon(k):
    return "Yes" if k % 2 == 0 else "No"

k = int(input())
print(watermelon(k))


# Way Too Long Words
def longWords(word):
    if len(word) > 10:
        return word[0] + str(len(word) - 2) + word[len(word) - 1]
    else:
        return word
    
word = str(input())
print(longWords(word))


# Boy or Girl
def boyOrGirl(name):
    return "CHAT WITH HER!" if len(set(name)) % 2 == 0 else "IGNORE HIM!"

name = str(input())
print(boyOrGirl(name))

# Search The 0 Sums Combinations in an Array
from itertools import combinations

def find_zero_sum_groups(arr, n):
    if not arr:
        return "No elements to combine"
    
    result = set()
    for cmb in combinations(sorted(arr), n):
        if sum(cmb) == 0:
            result.add(tuple(cmb))
            
    if not result:
        return "No combinations"
    
    return sorted(map(list, result))