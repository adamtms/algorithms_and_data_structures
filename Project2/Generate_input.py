import random

def generateRandom(n=5_000, rang=None):
    if rang is None:
        rang = n*10
    result = random.sample(range(rang), n)
    return result

def generateCondense(n=5_000):
    result = generateRandom(n, n//10)
    return result

def generateSparse(n=5_000):
    result = generateRandom(n, n*1000)
    return result

def generateIncreasing(n=5_000, rang=None):
    result = generateRandom(n, rang)
    result.sort()
    return result

def generateDecreasing(n=5_000, rang=None):
    result = generateRandom(n, rang)
    result.sort(reverse=True)
    return result

def generateVShape(n=5_000, rang=None):
    first = []
    last = []
    result = generateDecreasing(n, rang)
    for i, value in enumerate(result):
        if i % 2 == 0:
            first.append(value)
        else:
            last.append(value)
    return first + last[::-1]