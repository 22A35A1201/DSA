from collections import deque
def reverse(q):
    d=deque()
    for i in range(len(q)):
        d.appendleft(q.popleft())
    for j in range(len(d)):
        q.append(d.popleft())
    
    
q=deque()
q.append(10)
q.append(20)
q.append(30)
q.append(40)
q.append(50)


reverse(q)
print(q)