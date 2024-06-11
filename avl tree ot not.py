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
    height(root.left)
    height(root.right)
    
    lheight=height(root.left)
    rheight=height(root.right)

    if abs(lheight-rheight)<=1:
        return True
    else:
        return False

    if lheight>rheight:
        return 1+lheight
    
    else:
        return 1+rheight
    

    
height(root)
print(height(root))
