# The latest clock
from itertools import permutations

def late_clock(a, b, c, d):
    digits = [a, b, c, d]

    valid_times = ["".join(map(str, perm)) for perm in permutations(digits)]

    valid_times = [time for time in valid_times if 0 <= int(time[:2]) <= 23 and 0 <= int(time[2:]) <= 59]

    if not valid_times:
        return "Invalid input: Unable to form a valid time."

    latest_time = max(valid_times)

    return f"{latest_time[:2]}:{latest_time[2:]}"

# Is Integer Array?
def is_int_array(arr):
    if arr is None or arr == '':
        return False
    if not hasattr(arr, '__iter__'):
        return False
    for i in arr:
        if not isinstance(i, (int, float)) or (isinstance(i, float) and i % 1 != 0):
            return False
    return True

# Create a frame!
def frame(text, char):
    max_length = max(len(word) for word in text)
    
    frame_top = char * (max_length + 4)
    frame_bottom = char * (max_length + 4)
    
    result = [frame_top]
    
    for word in text:
        spaces = max_length - len(word)
        result.append(f"{char} {word}{' ' * spaces} {char}")
        
    result.append(frame_bottom)
    
    return '\n'.join(result)