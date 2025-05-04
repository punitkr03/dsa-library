def getFloorCeil(nums, x):
    l = 0
    r = len(nums) - 1
    ceil_val= -1
    floor_val = -1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == x:
            return x, x
        elif nums[mid] < x:
            floor_val = nums[mid]
            l = mid + 1
        else:
            ceil_val = nums[mid]
            r = mid - 1
    return floor_val, ceil_val

# AI generated test-cases, the above code is not AI slop though
test_cases = [
    # Basic cases
    ([1, 2, 4, 6, 10], 5, (4, 6)),      # Normal between elements
    ([1, 2, 4, 6, 10], 4, (4, 4)),      # Exact match
    ([1, 2, 4, 6, 10], 0, (-1, 1)),     # Smaller than all
    ([1, 2, 4, 6, 10], 11, (10, -1)),   # Greater than all

    # Edge cases
    ([5], 5, (5, 5)),                   # Single element match
    ([5], 4, (-1, 5)),                  # Single element, smaller
    ([5], 6, (5, -1)),                  # Single element, larger
    ([], 5, (-1, -1)),                  # Empty array

    # Duplicates
    ([1, 2, 2, 2, 3], 2, (2, 2)),       # Duplicates, exact match
    ([1, 2, 2, 2, 3], 1, (1, 1)),       # Duplicates, lower bound
    ([1, 2, 2, 2, 3], 3, (3, 3)),       # Duplicates, upper bound
    ([1, 2, 2, 2, 3], 0, (-1, 1)),      # Below all duplicates
    ([1, 2, 2, 2, 3], 4, (3, -1)),      # Above all duplicates
]


for nums, x, expected in test_cases:
    result = getFloorCeil(nums, x)
    print(f"Input: nums={nums}, x={x} → Output: {result}, Expected: {expected}, {'✅' if result == expected else '❌'}")

