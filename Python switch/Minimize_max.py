import math
def minimizedMaximum(n, quantities):
    """
    :type n: int
    :type quantities: List[int]
    :rtype: int
    """
    def can_distribute(x):
        stores = 0
        for quantity in quantities:
            stores += math.ceil(quantity / x)
        return stores <= n
    
    res = 0
    l,r = 1, max(quantities)

    while l <= r:
        mid = (l + r) // 2
        print(can_distribute(mid))
        if can_distribute(mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

print(minimizedMaximum(n=1, quantities=
[1000000]))