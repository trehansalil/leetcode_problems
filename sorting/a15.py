# https://leetcode.com/tag/sorting/
from typing import List, Set, Any


# https://leetcode.com/problems/3sum/

# Runtime
# 544
# ms
# Beats
# 92.57%
# of users with Python3
# Memory
# 20.36
# MB
# Beats
# 93.69%
# of users with Python3

class Solution:
    def __init__(self):
        self.res = set()

    def twoSum(self, nums, i):
        l, r = i + 1, len(nums) - 1
        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum < 0:
                l += 1
            elif curr_sum > 0:
                r -= 1
            elif curr_sum == 0:
                self.res.add((nums[i], nums[l], nums[r]))
                l += 1

    def threeSum(self, nums: List[int]) -> set[Any]:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                self.twoSum(nums, i)
        return self.res

