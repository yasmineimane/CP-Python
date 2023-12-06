# Highest Scoring Word
def high(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    count = [sum([alphabet.find(i) + 1 for i in word]) for word in x.split()]
    return x.split()[count.index(max(count))]

# Basic Encryption
def encrypt(text, rule):
    encrypted_text = ''

    for char in text:
        if char.isprintable():
            encrypted_text += chr((ord(char) + rule) % 128)
        else:
            encrypted_text += char

    return encrypted_text