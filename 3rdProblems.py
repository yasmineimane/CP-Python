# Leap Years
def is_leap_year(year):
    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

# Bit Counting
def count_bits(n):
    return bin(n).count("1")

# Persistent Bugger
def persistence(n):
    counter = 0
    while n >= 10:
        pres = 1
        for nbr in str(n):
            pres *= int(nbr)
        counter += 1
        n = pres
    return counter

# Matrix Transpose
def transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    for r in result:
        return result