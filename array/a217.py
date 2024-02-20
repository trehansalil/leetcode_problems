# https://leetcode.com/tag/arrays/
from typing import List, Any


# https://leetcode.com/problems/contains-duplicate/description/

# Runtime: 418 ms
# Beats 71.53% of users with Python3

# Memory: 31.86 MB
# Beats 90.78% of users with Python3

class Solution:
    def __init__(self):
        self.ans_bool = False

    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
                if hashmap[num] > 1:
                    return True
            else:
                hashmap[num] = 1
        return self.ans_bool
