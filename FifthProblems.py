# Equal Sides Of An Array
def find_even_index(arr):
    for i in range(0, len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


# Playing with digits
def dig_pow(n, p):
    num = str(n)
    total = sum([int(num[i]) ** (p + i) for i in range(len(num))])
    return total / n if (total % n) == 0 else -1


# Who likes it
def likes(names):
    whoLikesIt = ""
    
    if (len(names) == 0):
        whoLikesIt = "no one likes this"
    elif (len(names) == 1):
        whoLikesIt = names[0] + " likes this"
    elif (len(names) > 1 and len(names) < 4):
        for name in range(0, len(names) - 1):
            whoLikesIt += names[name] + ", "
        whoLikesIt = whoLikesIt[:-2]
        whoLikesIt += " and " + names[len(names) - 1] + " like this"
    else:
        for name in range(0, 2):
            whoLikesIt += names[name] + ", "
        whoLikesIt = whoLikesIt[:-2]
        whoLikesIt += " and " + str(len(names) -2) + " others like this"
    return whoLikesIt


# Your order, please
def order(sentence):
    words = []
    
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word:
                words.append(word)
    return " ".join(words)
