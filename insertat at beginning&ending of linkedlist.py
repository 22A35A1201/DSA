class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def display(temp):
    while temp!=None:
        print(temp.data)
        temp=temp.next

def insert_big(data,head):
    newNode=Node(data)
    newNode.next=head
    head=newNode
    return head
def insert_end(data,head):
    newNode2=Node(data)
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=newNode2
    



head=Node(1)
second = Node(2)
third = Node(3)
four=Node(4)
fifth=Node(5)
head.next=second

second.next=third
third.next=four
four.next=fifth
display(head)
head=insert_big(150,head)
display(head)
fifth=insert_end(100,head)
display(head)






