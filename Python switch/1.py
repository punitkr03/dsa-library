class Solution:
    def twoSum( nums: list[int], target: int) -> list[int]:
        valueHashmap = {} #value : idx
        for i, n in enumerate(nums):
            difference = target - n
            if difference in valueHashmap:
                print(valueHashmap[difference])
                return [valueHashmap[difference], i]
            else:
                valueHashmap[n] = i
                print(valueHashmap)