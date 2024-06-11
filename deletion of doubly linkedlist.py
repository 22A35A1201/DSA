class Node:
    def __init__(self,data):
        self.data=data
        self.next=None




def display(head):
    temp=head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
    return head
def deletion(s,d,head):
    temp=head
    s1=1
    d1=0
    while temp!=None and s1<s:
        temp=temp.next
        s1+=1
    store_temp=temp
    while temp!=None and d1<d:
        temp=temp.next
        d1+=1
    store_temp.next=temp.next
    return head


head=Node(4)
second = Node(7)
third = Node(9)
four=Node(20)
head.next=second
second.next=third
third.next=four


display(head)
deletion(1,1,head)



