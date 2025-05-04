class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        minptr = 0
        maxptr = len(numbers) - 1

        while(minptr < maxptr):
            if(numbers[minptr] + numbers[maxptr] == target):
                return [minptr+1, maxptr+1]
            elif (numbers[minptr] + numbers[maxptr] > target):
                maxptr -= 1
            else:
                minptr += 1