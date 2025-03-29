def binary_search(arr,low,high,tar):
    if(low<=high):
        mid=(low+high) // 2

        if(arr[mid]==tar):
            return mid
        elif(tar>arr[mid]):
            return binary_search(arr,mid+1,high,tar)
        elif(tar<arr[mid]):
            return binary_search(arr,low,mid-1,tar)
        else:
            return -1

n=int(input())
arr=list(map(int, input().split()))
tar=int(input())
res=binary_search(arr,0,len(arr)-1,tar)
if res==-1:
    print("tar not found")

else:
    print("tar found at :", res)
    
