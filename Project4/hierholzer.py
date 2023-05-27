from collections import defaultdict

def hierholzer(graph):
    # Step 1: Check if the graph has an Eulerian cycle
    if not is_eulerian(graph):
        return None

    # Step 2: Choose a starting vertex
    start_vertex = next(iter(graph.nodes.keys()))

    # Step 3: Initialize stack and empty path
    stack = [start_vertex]
    path = []

    while stack:
        v = stack[-1]

        if graph.nodes[v]:
            # Step 4: Find a cycle starting from v
            u = graph.nodes[v].pop()
            stack.append(u)

            # Step 5: Remove the edge between v and u
            graph.nodes[u].remove(v)
        else:
            # Step 6: Backtrack when there are no more unvisited edges from v
            path.append(stack.pop())

    # Step 7: Return the reversed path
    return path[::-1]


def is_eulerian(graph):
    # Step 1: Check if all vertices have even degree
    for v in graph.nodes.keys():
        if len(graph.nodes[v]) % 2 != 0:
            return False

    # Step 2: Check if the graph is connected
    visited = set()

    def dfs(v):
        visited.add(v)
        for neighbor in graph.nodes[v]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(1) 

    if len(visited) != len(graph.nodes.keys()):
        return False

    return True
