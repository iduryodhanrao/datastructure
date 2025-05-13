
"""
Asymptotic complexity in terms of total number of nodes in the given tree `n`:
* Time: O(n).
* Auxiliary space: O(n).
* Total space: O(n).
"""


def preorder_recursive(current_node, result):
    if current_node is None:
        return

    result.append(current_node.value)
    preorder_recursive(current_node.left, result)
    preorder_recursive(current_node.right, result)


def preorder(root):
    result = []
    preorder_recursive(root, result)
    return result

# Example usage
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Constructing a binary tree
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
# Preorder traversal
result = preorder(root)
print("Preorder Traversal Result:")
print(result)
# Output: [1, 2, 4, 5, 3, 6, 7]