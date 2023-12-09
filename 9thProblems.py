# Find the missing letter
def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        current_ord = ord(chars[i])
        next_ord = ord(chars[i + 1])
        if next_ord - current_ord > 1:
            return chr(current_ord + 1)
        
# Is a number prime
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

# Valid Braces
def valid_braces(string):
    stack = []
    open_braces = {'(', '[', '{'}
    close_braces = {')' : '(', ']' : '[', '}' : '{'}
    
    for char in string:
        if char in open_braces:
            stack.append(char)
        if char in close_braces:
            if not stack or stack.pop() != close_braces[char]:
                return False
            
    return not stack