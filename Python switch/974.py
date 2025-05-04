class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range (len(nums)):
            start = 0
            end = i
            for j in range (len(nums)-i):
                temp = nums.slice(start : end)
                if(sum(temp) % k == 0):
                    res += 1
                start += i
                end += i