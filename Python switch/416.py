from typing import List
def canPartition(nums: List[int]) -> bool:
    sum = 0
    for n in nums:
        sum += n
    if sum & 1:
        return False
    target = sum // 2
    dp = set()
    for i in range(len(nums)-1, -1, -1):
        for num in dp:
            sum = num + nums[i]
            if sum not in dp:
                dp.add(sum)
    if target in dp:
        return True
    return False

print(canPartition(nums=[1,5,11,5]))