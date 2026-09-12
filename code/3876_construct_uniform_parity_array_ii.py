# Problem: Construct Uniform Parity Array II
# Topic: Math
# Difficulty: Medium
import sys


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        is_odd = False
        min_odd = sys.maxsize
        min_even = sys.maxsize
        for i in nums1:
            if i % 2 == 1:
                is_odd = True
                min_odd = min(min_odd, i)
            else:
                min_even = min(min_even, i)
        if not is_odd:
            return True
        return min_even > min_odd
