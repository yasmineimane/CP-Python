# Write Number in Expanded Form
def expanded_form(num):
    result = []
    
    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            result.append(digit + ('0' * index))
            
    return ' + '.join(result[::-1])

# Simple Encryption #1 - Alternating Split
def encrypt(text, n):
    if not text or n <= 0:
        return text

    for _ in range(n):
        text = text[1::2] + text[0::2]

    return text

def decrypt(encrypted_text, n):
    if not encrypted_text or n < 0:
        return encrypted_text

    length = len(encrypted_text)
    mid = length // 2

    for _ in range(n):
        decrypted_text = [''] * length

        for i in range(mid):
            decrypted_text[i * 2] = encrypted_text[i + mid]
            decrypted_text[i * 2 + 1] = encrypted_text[i]
        
        if length % 2 == 1:
            decrypted_text[length - 1] = encrypted_text[length - 1]

        encrypted_text = ''.join(decrypted_text)

    return encrypted_text

# Help the bookseller !
import re
def stock_list(list_of_art, list_of_cat):
    total = dict()
    string = str()
    for letter in list_of_cat:
        regex = re.compile(r'^('+letter+').*\s(\d+)')
        for code in list_of_art:
            mo = regex.findall(code)
            if mo:
                total[mo[0][0]] = total.get(mo[0][0], 0) + int(mo[0][1])
            else:
                total[letter] = total.get(letter, 0)
    for key, value in total.items():
        string += f'({key} : {value}) - '
    return string.rstrip(' - ') 