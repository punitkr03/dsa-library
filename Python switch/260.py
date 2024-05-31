class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for item in nums:
            diff ^= item
        bit_position = 0
        while not diff & (1 << bit_position): 
            bit_position += 1
        first = 0
        for item in nums:
            if item & (1 << bit_position):
                first ^= item
        return [first, first ^ diff]
        