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

'''
def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.data:
        root.left=insert(root.left,key)
    elif key>root.data:
        root.right=insert(root.right,key)
    return root
'''

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.key)
    inorder(root.right)
    '''
    if root:
        res=inorder(root.left)
        res.append.root.data
        res=res+inorder(root.right)
    return root
    '''
def preorder(root):
    if root is None:
        return
    print(root.key)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    inorder(root.left)
    inorder(root.right)
    print(root.key)

inorder(root)
preorder(root)
postorder(root)