# # Helpful Maths
def helpfulMaths(calcule):
    return '+'.join(['1']*calcule.count('1') + ['2']*calcule.count('2') + ['3']*calcule.count('3'))

calcule = input()
print(helpfulMaths(calcule))

# Team
def team(n, problems):
    count = 0
    for problem in problems:
        if problem.count(1) >= 2:
            count += 1
    return count

n = int(input("Enter a number: "))
problems = [list(map(int, input().split())) for _ in range(n)]
print(team(n, problems))

# Word Capitalization
def wordCapitalization(word):
    return word[0].upper() + word[1:]

word = input()
print(wordCapitalization(word))