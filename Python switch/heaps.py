import heapq
def rank(arr):
    n = len(arr)
    temp = []
    hashmap = {}
    for i in range(n):
        heapq.heappush(temp, arr[i])
    i = 1
    while temp:
        hashmap[heapq.heappop(temp)] = i
        i += 1
    res = []
    for num in arr:
        res.append(hashmap[num])
    return res

print(rank([20,15,26,2,98,6]))