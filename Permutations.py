def perm1(arr):
    if len(arr)==0 or len(arr)==1:
        return [arr]

    else:
        l = []
        for x in range(len(arr)):
            i  = arr[x]
            ix = arr[0:x]+arr[x+1:]
            for p in perm1(ix):
                l.append([i]+p)
        return l
#This algorithm is crappy. It has back time complexity and a bad space complexity. I can convert this into a generator to make the space complextiy much smallet
#but I would still have a terrible time complexity. I could probably use a hash table to fix it and make it run in O(n) time.
