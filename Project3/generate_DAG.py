import random

# Generate nested list, if elem in position x, y is equal to:
#   -1, exists edge from y to x
#    1, exists egde from x to y
#    0, doesn't exists edge between x and y
# Nodes are indexed from 0
def generateDAG(nodesNum: int=100):
    initial_matrix = [[0 for _ in range(x+1)] + [1 for _ in range(nodesNum - x - 1)] for x in range(nodesNum)]
    nodes = [i for i in range(nodesNum)]
    random.shuffle(nodes)
    matrix = [[0 for _ in range(nodesNum)] for _ in range(nodesNum)]
    for startNodeIndex in range(nodesNum):
        for endNodeIndex in range(nodesNum):
            matrix[startNodeIndex][endNodeIndex] = initial_matrix[nodes[startNodeIndex]][nodes[endNodeIndex]]
    return matrix