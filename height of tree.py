class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

root=Node(1)
first=Node(2)
second=Node(3)
third=Node(4)
fourth=Node(5)
fifth=Node(6)
sixth=Node(7)

root.left=first
root.right=second
first.left=third
first.right=fourth
second.left=fifth
second.right=sixth

def height(root):
    if root is None:
        return 0
    
    lheight=height(root.left)
    rheight=height(root.right)

    if lheight>rheight:
        return 1+lheight
    
    else:
        return 1+rheight
    
'''    
def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.key)
    inorder(root.right)
    '''

    
height(root)
print(height(root))
