l=[81,9,4,14,2]
for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)
        
