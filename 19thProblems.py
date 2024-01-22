# # Odd Divisor
# def oddDivisor(n):
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0 and i % 2 == 1:
#             return "Yes"
#     return "No"

# # Sale
# def sale(n, m, prices):
#     prices.sort()
#     money = sum(min(price, 0) for price in prices[:m])
#     return abs(money)

# n, m = map(int, input().split())
# prices = list(map(int, input().split()))
# print(sale(n, m, prices))

# # New Year's Number
# def newYearNumber(n):
#     if n < 2020:
#         return "No"
#     m = n % 2020
#     if m == 1 or (m % 2) == 0:
#         return "Yes"
#     return "No"

# t = int(input())
# result = []
# for _ in range(t):
#     n = int(input())
#     result.append(newYearNumber(n))

# print(result)

# Multiply by 2, divide by 6
def multipleOrDivide(n):
    if n == 1:
        return -1
    count = 0
    while (n > 1):
        if n % 6 == 0:
            n //= 6
        elif n % 3 == 0:
            n *= 2
        else:
            return -1
        count += 1
    return count

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    result.append(multipleOrDivide(n))

print(result)

