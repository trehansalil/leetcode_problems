# https://leetcode.com/tag/arrays/
from typing import List


# https://leetcode.com/problems/missing-number/

# Runtime: 97 ms
# Beats 98.68% of users with Python3

# Memory: 17.59 MB
# Beats 99.86% of users with Python3

class Solution:
    def __init__(self):
        self.np_int = 0

    def missingNumber(self, nums: List[int]) -> int:
        while self.np_int in nums:
            self.np_int += 1

        return self.np_int

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int((n*(n+1))/2 - sum(nums))