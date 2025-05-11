"""
Asymptotic complexity in terms of the number of vertices `v` and number of edges `e` in the graph:
* Time: O(v + e).
* Auxiliary space: O(v + e).
* Total space: O(v + e).
"""

from collections import deque

def bfs_traversal_helper(start_node, graph, is_visited, answer):
    is_visited[start_node] = True
    answer.append(start_node)
    q = deque([start_node])

    while q:
        u = q.popleft()

        for v in graph[u]:
            if not is_visited[v]:
                answer.append(v)
                q.append(v)
                is_visited[v] = True

def bfs_traversal(n, edges):
    graph = [[] for _ in range(n)]
    is_visited = [False] * n
    answer = []

    # Making a graph from the input edges.
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for i in range(n):
        if not is_visited[i]:
            bfs_traversal_helper(i, graph, is_visited, answer)

    return answer

if __name__ == "__main__":
    # Example usage
    n = 5  # Number of vertices
    edges = [
            [0, 1],
            [1, 4],
            [1, 2],
            [1, 3],
            [3, 4]
            ]
    bfs_traversal_result = bfs_traversal(n, edges)
    print("BFS Traversal Result:")
    print(bfs_traversal_result)