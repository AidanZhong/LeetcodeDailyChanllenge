# Problem: Longest Subsequence With Non-Zero Bitwise XOR
# Topic: Bit manipulation
# Difficulty: Medium
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        contains_non_zero = False
        xor_total = 0
        for i in nums:
            if i != 0:
                contains_non_zero = True
                xor_total ^= i

        if xor_total != 0:
            return n
        elif contains_non_zero:
            return n - 1
        else:
            return 0
