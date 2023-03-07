from random import randint
def generateInput():
    result = []
    n = int(1e5)
    for _ in range(n):
        result.append(randint(0, n))
    return result