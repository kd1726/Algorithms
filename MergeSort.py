def Merge(a,b):
    c = []
    a_idx,b_idx=0,0
    while a_idx<len(a) and b_idx<len(b):
        if a[a_idx]<b[b_idx]:
            c.append(a[a_idx])
            a_idx+=1
        else:
            c.append(b[b_idx])
            b_idx+=1
    if len(a)==a_idx:
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    return c

def MergeSort(arr):
    if len(arr)==1 or len(arr)==0:
        return arr
    else:
        dv = len(arr)//2
        left,right = MergeSort(arr[0:dv]),MergeSort(arr[dv:])
        return Merge(left,right)
