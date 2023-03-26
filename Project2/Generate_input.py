import random

def generateRandom(n=5_000, rang=None, data = None):
    if rang is None:
        rang = n*10
    if not data:
        data = random.sample(range(rang), n)
    else:
        random.shuffle(data)
    return data

def generateIncreasing(n=5_000, data = None, rang=None):
    if not data:
        data = generateRandom(n, rang = rang)
    data.sort()
    return data

def generateDecreasing(n=5_000, data = None, rang=None):
    if not data:
        data = generateRandom(n, rang = rang)
    data.sort(reverse=True)
    return data

def generateVShape(n=5_000, data = None, rang=None):
    if not data:
        data = generateDecreasing(n, rang = rang)
    first = []
    last = []
    for i, value in enumerate(data):
        if i % 2 == 0:
            first.append(value)
        else:
            last.append(value)
    return first + last[::-1]