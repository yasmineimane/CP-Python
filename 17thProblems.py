# Next Round
def nextRound(arr, n, k):
    if all([ v == 0 for v in arr ]) :
        return 0
    elif arr[k] >= arr[k - 1]:
        return k + 1
    else:
        return k
    
arr = int(input())
n = int(input())
k = int(input())
print(nextRound(arr, n, k))

# Bit++
def bit(n, statements):
    x = 0
    for statement in statements:
        if "++" in statement:
                x += 1
        elif "--" in statement:
                x -= 1
    
    return x

n = int(input("Enter a number :"))
statements = [input() for _ in range(n)]
print(bit(n, statements))


# Domino piling
def dominoPiling(m, n):
    return int((m * n) / 2)

m = int(input())
n = int(input())
print(dominoPiling(m, n))


# Petya and Strings
def petya(str1, str2):
    if str1.lower() == str2.lower():
        print(0)
    elif str1.lower() > str2.lower():
        print(1)
    else:
        print(-1)

str1 = input()
str2 = input()
petya(str1, str2)