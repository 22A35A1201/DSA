'''from collections import deque
dq=deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
dq.append(5)


for i in range(len(dq)):
    s.append(dq.popleft())

for i in range(len(dq)):
    dq.append(s.pop())

print(dq)'''

from collections import deque
q=deque()
q.append('a')
q.append('b')
q.append('c')
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)

