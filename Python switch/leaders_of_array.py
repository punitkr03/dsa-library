def find_leaders(arr):
    curr = arr[-1]
    res = [arr[-1]]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= curr:
            res.append(arr[i])
            curr = arr[i]
    res.reverse()
    return res

arr = [10, 4, 2, 4, 1]
print(find_leaders(arr))