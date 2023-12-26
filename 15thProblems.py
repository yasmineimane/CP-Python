# Roman Numerals Encoder
def solution(n):
    roman_dict = {
        1000 : 'M',
        900 : 'CM',
        500 : 'D',
        400 : 'CD',
        100 : 'C',
        90 : 'XC',
        50 : 'L',
        40 : 'XL',
        10 : 'X',
        9 : 'IX',
        5 : 'V',
        4 : 'IV',
        1 : 'I',
    }
    
    result = ''
    
    for value, symbol in sorted(roman_dict.items(), key=lambda x : x[0], reverse= True):
        while n >= value:
            result += symbol
            n -= value
    
    return result

# Roman Numerals Decoder
def solution(roman: str) -> int:
    roman_numerals = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    result = 0
    i = 0
    
    while i < len(roman):
        if i + 1 < len(roman) and roman[i: i+2] in roman_numerals:
            result += roman_numerals[roman[i : i+2]]
            i += 2
        else:
            result += roman_numerals[roman[i]]
            i += 1
            
    return result

# IP Validation
def is_valid_IP(strng):
    nums = strng.split('.')
    
    if len(nums) == 4 and all(0 <= int(i) <= 255 and str(int(i)) == i if i.isdigit() else False for i in nums):
        return True
    else:
        return False