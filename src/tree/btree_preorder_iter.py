"""
Asymptotic complexity in terms of total number of nodes in the given tree `n`:
* Time: O(n).
* Auxiliary space: O(n).
* Total space: O(n).
"""


def preorder(root):
    result = []
    if root is None:
        return result

    # This stack will replicate the functionalities of the recursive call stack.
    stack = []

    stack.append(root)
    print("Stack:", stack[0].value)

    while stack:
        current = stack.pop()
        print("Current:", current.value)
        result.append(current.value)

        # Since a stack follows the property of last-in-first-out, the node inserted later will be popped
        # out first.
        # Therefore, we are first appending the right child and then the left child of the current node.
        # This way, left child will be popped out before the right child.
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result
# Example usage
class BtNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Constructing a binary tree
root = BtNode(1)
root.left = BtNode(2)
root.right = BtNode(3)
root.left.left = BtNode(4)
root.left.right = BtNode(5)
root.right.left = BtNode(6)
root.right.right = BtNode(7)
# Preorder traversal
result = preorder(root)
print("Preorder Traversal Result:")
print(result)
# Output: [1, 2, 4, 5, 3, 6, 7]
