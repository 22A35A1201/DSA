L=[2,1,2,2,0,1,2,0,0,1,1]
c1=0
c2=0
c3=0
for i in range(0,len(L)):
    if L[i]==0:
        c1+=1
    elif L[i]==1:
        c2+=1
    elif L[i]==2:
        c3+=1
index=0
while c1!=0:
    L[index]=0
    c1-=1
    index+=1
while c2!=0:
    L[index]=1
    c2-=1
    index+=1
while c3!=0:
    L[index]=2
    c3-=1
    index+=1
print(L)    
    
    