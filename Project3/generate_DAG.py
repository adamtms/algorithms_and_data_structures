def generating_matrix(nodes_num: int=100):
    matrix = [[0 for _ in range(x + 1)] + [1 for _ in range(nodes_num - x - 1)] for x in range(nodes_num)]
    print(*matrix, sep="\n")

generating_matrix(10)