matrix = [[1,1,1],[1,0,1],[1,1,1]]

idxHashmap = {}
for i, n in enumerate(matrix):
    if i in idxHashmap:
        continue
    for j, p in enumerate(n):
        if(p==0):
            print(i, j)
            for k in range (0, len(n)):
                matrix[i][k] = 0
            for l in range (0, len(matrix)):
                matrix[l][j] = 0
            if(i not in idxHashmap):
                idxHashmap[i] = j
            print(idxHashmap)
print(matrix)