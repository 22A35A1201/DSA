
def peakvalue(arr):
    s=0
    e=len(arr)-1
    mid=s+(e-s)//2
    while s<=e:
        if (arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
            ans=mid
            break
        elif (mid>0 and arr[mid-1]>arr[mid]):
            e=mid
        elif arr[mid]<arr[mid+1]:
            s=mid
        mid=s+(e-s)//2
    print(ans)
peakvalue([1,3,6,7,9,5,2])
