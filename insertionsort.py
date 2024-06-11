def insertion(arr,size):
    for i in range(1,size):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
arr=[23,76,13,65,26]
size=len(arr)
insertion(arr,size)
print(arr)
