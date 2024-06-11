class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return TreeNode(key)
    
    # Otherwise, recur down the tree
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    # return the (unchanged) node pointer
    return root

def findMaxNode(root):
    # Initialize current node as root
    current = root
    
    # Loop down to find the rightmost leaf
    while current.right is not None:
        current = current.right
    
    return current

# Helper function to print the tree
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=' ')
        inorderTraversal(root.right)

# Driver code
if __name__ == "__main__":
    root = None
    keys = [20, 8, 22, 4, 12, 10, 14]

    for key in keys:
        root = insert(root, key)
    
    print("Inorder traversal of the given tree: ")
    inorderTraversal(root)
    print()
    
    maxNode = findMaxNode(root)
    print(f"The maximum node value in the BST is: {maxNode.val}")
