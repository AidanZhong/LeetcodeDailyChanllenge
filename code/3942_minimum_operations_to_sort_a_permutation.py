# Problem: Minimum Operations to Sort a Permutation
# Topic: String
# Difficulty: Medium
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        mini_idx = nums.index(0)
        max_idx = nums.index(n - 1)
        if (mini_idx - 1) % n == max_idx:  # increasing
            for offset in range(1, n - 1):
                if nums[(mini_idx + offset) % n] < nums[(mini_idx + offset - 1) % n]:
                    return -1
            # move the biggest to the end
            return min((max_idx + 1) % n, n - mini_idx + 2)
        elif (max_idx - 1) % n == mini_idx:  # decreasing
            for offset in range(1, n - 1):
                if nums[(max_idx + offset) % n] > nums[(max_idx + offset - 1) % n]:
                    return -1
            # move the biggest to the front
            return min(max_idx + 1, n - mini_idx)  # plus the reverse
        else:
            return -1

