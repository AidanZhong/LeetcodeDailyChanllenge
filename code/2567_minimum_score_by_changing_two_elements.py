# Problem: Minimum Score by Changing Two Elements
# Topic: Greedy
# Difficulty: Medium
from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return min(
            nums[n - 1] - nums[2],  # change the two smallest numbers
            nums[n - 3] - nums[0],  # change the two largest numbers
            nums[n - 2] - nums[1],  # change the smallest and largest numbers
        )

