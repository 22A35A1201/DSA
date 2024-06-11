def knap(val,w,c,n):
    if c==0 or n==0:
        return 0
    if w[n-1]>c:
        return knap(val,w,c,n-1)
    else:
        return max(val[n-1]+knap(val,w,c-w[n-1],n-1),knap(val,w,c,n-1))
    
val=[60,100,120]
weight=[10,20,30]
capacity=50
print(knap(val,weight,capacity,len(weight)))