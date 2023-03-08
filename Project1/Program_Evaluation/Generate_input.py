from random import randint

def generate_random(n = int(1e4), rang=None):
    if rang is None:
        rang = n
    result = []
    for _ in range(n):
        result.append(randint(0, rang+1))
    return result

def generate_increasing(n = int(1e4), rang=None):
    result = generate_random(n, rang)
    result.sort()
    return result

def generate_decreasing(n = int(1e4), rang=None):
    result = generate_random(n, rang)
    result.sort(reverse=True)
    return result

def generate_v_shape(n = int(1e4), rang=None):
    half = n // 2
    first = generate_increasing(half, n)
    last = generate_decreasing(half, n)
    return first + last