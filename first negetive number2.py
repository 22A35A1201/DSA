from collections import deque
ip=[-4,-2,7,-5,-6,6]
d=deque()
w=2
n=len(ip)

for i in range(w):
    if ip[0]<0 and ip[0]<ip[1]:
        d.append(i)
    elif ip[1]<0 and ip[1]<ip[0]:
        d.append(i)

for i in range(w,n):
    if not d:
        print(0)
    else:
        print(ip[d[0]])
    while (d and i-d[0]>=w):
        d.popleft()
    if (ip[i]<0):
        d.append(i)
if (len(d)>0):
    print(ip[d[0]])
else:
    print(0)



