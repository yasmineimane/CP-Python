# One Variable Second Degree Equat
import math

def sec_deg_solver(a, b, c):
    match (a, b, c):
        case (0, 0, 0):
            return "The equation is indeterminate"
        case (0, 0, c):
            return "Impossible situation. Wrong entries"
        case (0, b, 0):
            return "It is a first degree equation. Solution: 0.0"
        case (0, b, c):
            return f"It is a first degree equation. Solution: {-c / b}"
        case (a, b, c):
            d = (b**2) - (4 * a * c)
            match d:
                case value if value > 0:
                    x1 = (-b - math.sqrt(d)) / (2 * a)
                    x2 = (-b + math.sqrt(d)) / (2 * a)
                    formatted_x1 = round(x1, 10)  
                    formatted_x2 = round(x2, 10)
                    return f"Two solutions: {formatted_x1}, {formatted_x2}"
                case value if value == 0:
                    x = -b / (2 * a)
                    return f"It has one double solution: {x}"
                case _:
                    return "There are no real solutions"
                
# What century is it
def what_century(year):
    century = (int(year) + 99) // 100
    
    if 10 <= century % 100 <= 20:
        suffix = 'th'
    else:
        last_digit = century % 10
        if last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
            
    return f'{century}{suffix}'

# Which are in
def in_array(array1, array2):
    result = []
    
    for s1 in array1:
        for s2 in array2:
            if s1 in s2:
                result.append(s1)
                break
    
    result.sort()
    return result