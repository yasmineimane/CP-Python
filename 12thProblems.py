# One down
def one_down(txt):
    if not isinstance(txt, str):
        return "Input is not a string"

    decoded_message = ""
    for char in txt:
        if char.isalpha():
            is_upper = char.isupper()

            decoded_char = chr((ord(char) - 1 - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            decoded_message += decoded_char
        else:
            decoded_message += char

    return decoded_message