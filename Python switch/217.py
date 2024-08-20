class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        print (nums)


Solution().containsDuplicate(nums=[1,2,3,1])