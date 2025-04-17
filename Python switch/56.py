class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        is_possible = False
        numset = set([])
        for n in nums:
            if n < k:
                return -1
            if n == k:
                is_possible = True
            numset.add(n)
        if !(is_possible):
            return -1
        

        return 1