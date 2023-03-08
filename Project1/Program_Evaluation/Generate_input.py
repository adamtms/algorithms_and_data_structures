from random import randint

def generate_random(n=5_000, rang=None):
    if rang is None:
        rang = n*10
    result = []
    for _ in range(n):
        result.append(randint(0, rang))
    return result

def generate_dense(n=5_000):
    result = generate_random(n, n//10)
    return result

def generate_sparse(n=5_000):
    result = generate_random(n, n*1000)
    return result

def generate_increasing(n=5_000, rang=None):
    result = generate_random(n, rang)
    result.sort()
    return result

def generate_decreasing(n=5_000, rang=None):
    result = generate_random(n, rang)
    result.sort(reverse=True)
    return result

def generate_v_shape(n=5_000, rang=None):
    first = []
    last = []
    result = generate_increasing(n, rang)
    for i, value in enumerate(result):
        if i % 2 == 0:
            first.append(value)
        else:
            last.append(value)
    return first + last[::-1]