"""
Asymptotic complexity in terms of the number of vertices `n` and number of edges `e` in the graph:
* Time: O(n * log(e)).
* Auxiliary space: O(1).
* Total space: O(n + e).
"""
def convert_edge_list_to_adjacency_list(n, edges):
    adjacency_list = [[] for _ in range(n)]

    for edge in edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])
    print(adjacency_list)

    for i in range(n):
        adjacency_list[i].sort()

    return adjacency_list

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
    adjacency_list = convert_edge_list_to_adjacency_list(n, edges)
    print("Adjacency List:")
    for i in range(n):
        print(f"{i}: {adjacency_list[i]}")