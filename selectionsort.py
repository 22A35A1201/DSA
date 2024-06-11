def selection(l,size):
    for i in range(size):
        min_idx=i
        for j in range(i+1,size):
            if l[min_idx]>l[j]:
                min_idx=j
            l[i],l[min_idx]=l[min_idx],l[i]

l=[23,36,4,12,18]
size=len(l)
selection(l,size)
print(l)