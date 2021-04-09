import math
def _partition(arr,l,r):
    pivot = arr[r]
    i = l
    for x in range(l,r):
        if arr[x]<=pivot:
            arr[x],arr[i]=arr[i],arr[x]
            i+=1
    arr[r],arr[i]=arr[i],arr[r]
    return i

def _kth_smallest(arr,l,r,k):
    if k>=0 and k<=r-l+1:
        index = _partition(arr,l,r)
        if index-l==k-1:
            return arr[index]
        elif index-l>k-1:
            return _kth_smallest(arr,l,index-1,k)
        else:
            return _kth_smallest(arr,index+1,r,k-index+l-1)
    return math.inf

def QuickSelect(arr,k):
    selected = _kth_smallest(arr,0,len(arr)-1,k)
    if selected!=math.inf:
        if k==1:
            return f"{selected} is the smallest element"
        elif k==2:
            return f"{selected} is the {k}nd smallest element"
        elif k==3:
            return f"{selected} is the {k}rd smallest element"
        else:
            return f"{selected} is the {k}th smallest element"
    else:
        return "nope"
