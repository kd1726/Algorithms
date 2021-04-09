def Heapify(arr,n,i):
    largest = i
    left_child = 2*i+1
    right_child = 2*i+2
    if left_child<n and arr[left_child]>=arr[largest]:
        largest = left_child
    if right_child<n and arr[right_child]>=arr[largest]:
        largest = right_child

    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        Heapify(arr,n,largest)

def HeapSort(arr):
    n  = len(arr)
    for x in range((len(arr)//2-1),-1,-1):
        Heapify(arr,n,x)
    for x in range(n-1,0,-1):
        arr[x],arr[0]=arr[0],arr[x]
        Heapify(arr,x,0)
    return arr
