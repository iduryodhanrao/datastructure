"""
Asymptotic complexity in terms of the number of vertices `n` and number of edges `e` in the graph:
* Time: O(e).
* Auxiliary space: O(1).
* Total space: O(n^2).
"""
def convert_edge_list_to_adjacency_matrix(n, edges):
    adjacency_matrix = [[False] * n for _ in range(n)]
    '''
    adjacency_matrix = [False] * n
    for i in range(n):
        adjacency_matrix[i] = [False] * n
    '''

    for edge in edges:
        adjacency_matrix[edge[0]][edge[1]] = True
        adjacency_matrix[edge[1]][edge[0]] = True

    return adjacency_matrix
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
    adjacency_matrix = convert_edge_list_to_adjacency_matrix(n, edges)
    print("Adjacency Matrix:")
    for row in adjacency_matrix:
        print(row)