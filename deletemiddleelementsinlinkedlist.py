class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def Display(head):
    temp=head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
def reverse(head,n):
    prev=None
    count=0
    print()
    while head!=None and count<n:
        next=head.next
        head.next=prev
        prev=head
        head=next
        count+=1
    if next!=None:
        head.next=reverse(next,n)
    return prev
    

    
head=Node(12)
n2=Node(23)
n3=Node(34)
n4=Node(54)
n5=Node(76)
n6=Node(87)
head.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
Display(head)
head=reverse(head,3)
Display(head)

