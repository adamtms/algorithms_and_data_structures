from random import randint
def generateInput(n = int(1e4)):
    result = []
    for _ in range(n):
        result.append(randint(0, n))
    return result