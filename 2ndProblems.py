
# Sum of two lowest positive integers
def sumTwoSmallest(numbers):
    numbers.sort(reverse = True)
    x = numbers.pop()
    y = numbers.pop()

    return x + y

# Regex validate PIN code
def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isnumeric():
        return True
    else:
        return False

# Binary Addition
import math

def add_binary(a,b):
    nbr = a + b
    bin = ''
    while nbr > 0:
        if nbr <= 1:
            bin += '1'
        if nbr > 1:
            if (nbr % 2 == 0):
                bin += '0'
            if nbr % 2 != 0:
                bin += '1'
        nbr = math.floor(nbr / 2)
        
    return bin[::-1]

# Is this a triangle?
def is_triangle(a, b, c):
    if ( a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    elif (a <= 0) or (b <= 0) or (c <= 0):
        return False
    else:
        return True
    
# The Coupon Code
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if (entered_code == correct_code) and (current_date > expiration_date):
        return True
    else:
        return False

# Fizz Buzz
def fizzbuzz(n):
    arr = []
    
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            arr.append("FizzBuzz")
        elif (i % 3 == 0):
            arr.append("Fizz")
        elif (i % 5 == 0):
            arr.append("Buzz")
        else:
            arr.append(i)

    return arr

# Convert string to camel case
def to_camel_case(text):
    text = text.replace("-", " ").replace("_", " ")
    words = text.split()
    return "".join([w.capitalize() if w != words[0] else w for w in words])

# Tribonacci Sequence
def tribonacci(signature, n):
    if n == 0:
        return []
    if n < 3:
        return [signature[i] for i in range(0,n)]
    res = signature[:]
    for i in range(3,n):
        res.append(res[i-1] + res[i-2] + res[i-3])
    return res

# The Hashtag Generator
def generate_hashtag(s):
    if len(s) == 0:
        return False
    else:
        result = "#" +'' .join(word.capitalize() for word in s.split(' '))
        if len(result) > 140:
            return False
        else:
            return result
