import random

def generateDAG(nodesNum: int=100, saturation: float = 1):
    initial_matrix = [[0] * (x + 1) + [1] * (nodesNum - x - 1) for x in range(nodesNum)]
    nodes = list(range(nodesNum))
    random.shuffle(nodes)
    matrix = [[0]*nodesNum for _ in range(nodesNum)]
    for startNodeIndex in range(nodesNum):
        for endNodeIndex in range(nodesNum):
            matrix[startNodeIndex][endNodeIndex] = 1 if (initial_matrix[nodes[startNodeIndex]][nodes[endNodeIndex]] and random.random() <= saturation) else 0
    return matrix