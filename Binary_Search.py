def binary_Search(arr,ele):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if ele<arr[mid]:
            high=mid-1
        elif ele>arr[mid]:
            low=mid+1
        else:
            return mid
    return -1

arr= [2,5,7,9,10,12]
res=binary_Search(arr,5)
if res!=-1:
    print('Element is present at:',res+1)
else:
    print('Element not Found...')

