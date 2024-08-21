class Solution(object):
    def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        curr_sum = 0
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        print(max_sum)
        
Solution.maxSubArray([-2,-3])