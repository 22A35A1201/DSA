l = [2,3,2,1,0,2]
t=len(l)-1
for i in range(t,-1,-1):
    if i+l[i] >= t:
        t=i
if t==0:
    print(True)
else:
    print(False)