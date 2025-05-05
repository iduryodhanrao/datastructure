class BinaryTreeNode_int32:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    """
    Perform in-order traversal of the binary tree and print each node's value.
    Args:
        root (BinaryTreeNode_int32): The root node of the binary tree.
    """
    if root is not None:
        # Traverse the left subtree
        inorder_traversal(root.left)
        # Print the current node's value
        print(root.value, end=" ")
        # Traverse the right subtree
        inorder_traversal(root.right)

def level_order_traversal(root):
    """
    Perform level-order traversal of the binary tree and print each node's value.
    Args:
        root (BinaryTreeNode_int32): The root node of the binary tree.
    """
    if root is None:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.value, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def search_node_in_bst(root, value):
    """
    Args:
     root(BinaryTreeNode_int32)
     value(int32)
    Returns:
     bool
    """
    if root is None:
            return False
    curr = root
    while curr is not None:
        if curr.value == value:
            return True
        if value > curr.value:
            curr = curr.right
        else:
            curr = curr.left
    return False
# Test cases
if __name__ == "__main__":
    # Example usage:
    # Constructing a simple binary search tree
    root = BinaryTreeNode_int32(10)
    root.left = BinaryTreeNode_int32(5)
    root.right = BinaryTreeNode_int32(15)
    root.left.left = BinaryTreeNode_int32(3)
    root.left.right = BinaryTreeNode_int32(7)
    root.right.right = BinaryTreeNode_int32(20)

    print("Binary Search Tree constructed.")
    # Performing in-order traversal
    print("In-order Traversal of the Binary Tree:")
    inorder_traversal(root)
    # Searching for a value in the BST
    value_to_search = 7
    result = search_node_in_bst(root, value_to_search)
    print(f"Value {value_to_search} found in BST: {result}")
