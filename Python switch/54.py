from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    l = t = 0
    r = len(matrix[0]) - 1
    b = len(matrix) - 1
    res = []

    while(l<=r and t<=b):
        for i in range(l, r + 1):
            res.append(matrix[t][i])
        t += 1
        if t > b:
            break
        for i in range(t, b + 1):
            res.append(matrix[i][r])
        r -= 1
        if l > r:
            break
        for i in range(r, l-1, -1):
            res.append(matrix[b][i])
        b -= 1
        if t > b:
            break
        for i in range(b, t - 1, -1):
            res.append(matrix[i][l])
        l += 1

spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
        