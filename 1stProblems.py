# Disemvowel Trolls
import re
def DisemvowelTrolls(comment):
    comment = re.sub("[aieouAIEOU]", "", comment)

    return comment

# String ends with
def StringEndsWith(str, end):
    return str.endswith(end)

# Square Every Digit
def square_digits(num):
    result = ''
    word = list(str(num))
    for char in word:
        result += str(int(char) ** 2)
    return int(result)

# Highest and Lowest
def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split()]

    return f"{max(numbers)} {min(numbers)}"

# Get the Middle Character
def getMiddle(string):
    if len(string) % 2 == 0:
        mid = int(len(string) / 2)
        return string[mid - 1 : mid + 1]
    else:
        mid = int(len(string) / 2)
        return string[mid: mid + 1]

# List Filtering
def filter_list(string):
    newList = []
    for i in string:
        if type(i) == int:
            newList.append(i)

    return newList

# You're a square!
import math
def isPerfectSquare(num):
    if num < 0:
        return False
    else:
        sqrt_num = math.sqrt(num)
        if sqrt_num.is_integer():  
            return True  
        else:  
            return False

# Exes and Ohs
def ExesAndOhs(string):
    xCount = 0
    oCount = 0
    for i in string:
        if i == 'x':
            xCount = xCount + 1
        else:
            oCount = oCount + 1
    if xCount == oCount:
        return True
    else:
        return False

# Jaden Casing Strings
import string
def JadenCasingStrings(str):
    return string.capwords(str)

# Complementary DNA
def ComplementaryDNA(DNA):
    output = ''

    for letter in DNA:
        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'C':
            output += 'G'
        elif letter == 'G':
            output += 'C'

    return output

# Stop gninnipS My sdroW!
def spin_words(sentence):
    words = sentence.split(" ")
    new_sentence = ""
    for i in words:
        if len(i) >= 5:
            new_sentence += (i[::-1])
        else:
            new_sentence += i
        if words.index(i) + 1 < len(words):
            new_sentence += " "
    return new_sentence