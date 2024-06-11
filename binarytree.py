class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key
    def trapreorder(self):
        print(self.value,end=" ")
        if self.left:
            self.left.trapreorder()
        if self.right:
            self.right.trapreorder()
    def trainorder(self):
        if self.left:
            self.left.trainorder()
        if self.right:
            self.right.trainorder()
        print(self.value,end=" ")
    def trapostorder(self):
        if self.left:
            self.left.trapostorder()
        print(self.value,end=" ")
        if self.right:
            self.right.trapostorder()
        
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)


print("preorder traversal:",end=" ")
root.trapreorder()
print("\ninorder traversal:",end=" ")
root.trapostorder()
print("\npost order traversal:",end=" ")
root.trainorder()