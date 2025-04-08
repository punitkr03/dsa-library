from collections import defaultdict
def subarr(nums : list, target: int ):
    n = len(nums)
    pre_xorr = defaultdict(int)
    xorr = 0
    pre_xorr[xorr] = 1 
    count = 0
    for n in nums:
        xorr ^= n
        x = xorr ^ target
        count += pre_xorr[x]
        pre_xorr[xorr] += 1
    return count




print (subarr(nums=[5, 6, 7, 8, 9], target=5))