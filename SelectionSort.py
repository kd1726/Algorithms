def SelectionSort(arr):
    sort = 0
    while sort<len(arr):
        min_value = None
        for i,val in enumerate(arr[sort:]):
            if min_value==None or val<arr[min_value]:
                min_value=sort+i
        arr[min_value],arr[sort]=arr[sort],arr[min_value]
        sort+=1
    return arr
