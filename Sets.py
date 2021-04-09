def combinationUtil(arr, n, r, index, data, i):
    if(index == r):
        l = []
        for j in range(r):
            l.append(data[j])
        print(l)
        return

    if(i >= n):
        return
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1, data, i + 1)
    combinationUtil(arr, n, r, index, data, i + 1)

def printcombination(arr, n, r):
    data = list(range(r))
    combinationUtil(arr, n, r, 0, data, 0)
