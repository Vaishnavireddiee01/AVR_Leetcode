#function for dividing

def divide(arr):
    if(len(arr)<=1):
        return arr
    
    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]

    sortleft=divide(lefthalf)
    sortright=divide(righthalf)

    return merge(sortleft,sortright)

#function for merging
def merge(left,right):
    ans=[]

    i=j=0
    while(i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            ans.append(left[i])
            i+=1

        else:
            ans.append(right[j])
            j+=1

    ans.extend(left[i:])
    ans.extend(right[j:])

    return ans

arr=list(map(int, input().split(",")))
s=divide(arr)
print(s)