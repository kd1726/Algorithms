def InsertionSort(arr):
    for i in range(1,len(arr)):
        cur_item = arr[i]
        cur_idx=i
        while cur_idx>0 and arr[cur_idx]<arr[cur_idx-1]:
            arr[cur_idx],arr[cur_idx-1]=arr[cur_idx-1],arr[cur_idx]
            cur_idx-=1
        cur_item = arr[cur_idx]
    return arr
