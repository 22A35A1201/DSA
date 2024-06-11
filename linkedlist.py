class Node:
    def __init__(self,data):
        self.data=data
        self.next=None




def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
    return head


head=Node(4)
second = Node(7)
third = Node(9)
four=Node(20)
head.next=second
second.next=third
third.next=four


display(head)


