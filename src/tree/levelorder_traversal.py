

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
Asymptotic complexity in terms of total number of nodes in the given tree `n`:
* Time: O(n).
* Auxiliary space: O(n).
* Total space: O(n).
"""
def bfs_level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here. 
    q = []
    ans = []
    if not root: return ans
    q.append(root)
    while q:
        temp_q = []
        res_q = []
        while q:
            node = q.pop(0)
            print(node.value)
            res_q.append(node.value)
            if node.left: temp_q.append(node.left)
            if node.right: temp_q.append(node.right)
        q = temp_q
        ans.append(res_q)
    return ans

"""
Asymptotic complexity in terms of total number of nodes in the given tree `n`:
* Time: O(n).
* Auxiliary space: O(n).
* Total space: O(n).
"""
def dfs(node, ret, level):
    if node is None:
        return

    if level >= len(ret):
        # This node is the first encountered node of its level
        # So allocating memory for storing the nodes of this level.
        # Note that we would not need to insert more than one row because we must have already
        # allocated memory for storing nodes from every level between 0 to (level[node.value] - 1).
        ret.append([])

    ret[level].append(node.value)

    # We would first explore the left child as we want to list the values from left to right
    dfs(node.left, ret, level + 1)
    dfs(node.right, ret, level + 1)


def dfs_level_order_traversal(root):
    ret = []
    dfs(root, ret, 0)
    return ret

# Test cases
if __name__ == "__main__":
    # Example usage:
    # Constructing a simple binary search tree
    root = BinaryTreeNode(4)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(6)
    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(5)
    root.right.right = BinaryTreeNode(7)

    # Perform level-order traversal
    print("Level-order traversal:")
    bfs_level_order_traversal(root)  # Output: 4 2 6 1 3 5 7
    print("DFS level-order traversal:")
    dfs_level_order_traversal(root)  # Output: [[4], [2, 6], [1, 3, 5, 7]]
