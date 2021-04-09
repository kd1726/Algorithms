#You can only use this on a sorted list

def BinarySearch(arr,target):
    if len(arr)==0 or (len(arr)==1 and arr[0]!=target):
        return "No result"
    dv = len(arr)//2
    pivot = arr[dv]
    if target<pivot:
        return BinarySearch(arr[:dv],target)
    elif target>pivot:
        return BinarySearch(arr[dv:],target)
    elif target==pivot:
        return f"{target} found in list"
    else:
        return "No result"
