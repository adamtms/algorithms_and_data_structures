import random

# Generate nested list, if elem in position x, y is equal to:
#   -1, exists edge from y to x
#    1, exists egde from x to y
#    0, doesn't exists edge between x and y
# Nodes are indexed from 0
def generateDAG(nodesNum: int=100):
    matrix = [[-1 for _ in range(x)] + [0] + [1 for _ in range(nodesNum - x - 1)] for x in range(nodesNum)]
    random.shuffle(matrix)
    return matrix