l=[12,24,45,67,68,89,99]
s=0
e=len(l)-1
mid=s+(e-s)//2 # to avoid integer limit
t=99
while s<=e:
    if t==l[mid]:
        ans=mid
        break
    elif t<l[mid]:
        e=mid-1
    elif t>l[mid]:
        s=mid+1
    mid=s+(e-s)//2
print(ans)
