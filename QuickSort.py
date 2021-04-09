def QuickSort(arr):
    from random import choice
    if len(arr)==0 or len(arr)==1:
        return arr

    else:
        pivot = arr[choice(range(0,len(arr)))]
        smaller,equal,bigger=[],[],[]

        for x in arr:
            if x<pivot:
                smaller.append(x)
            elif x>pivot:
                bigger.append(x)
            else:
                equal.append(x)
    return QuickSort(smaller)+equal+QuickSort(bigger)
