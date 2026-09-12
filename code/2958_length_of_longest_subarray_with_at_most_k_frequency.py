# Problem: Length of Longest Subarray With at Most K Frequency
# Topic: Sliding window
# Difficulty: Medium
from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        n = len(nums)
        count = defaultdict(int)
        max_len = 0
        while l <= r < n:
            # try to add nums[r] to the window
            count[nums[r]] += 1
            if count[nums[r]] <= k:
                max_len = max(max_len, r - l + 1)
                r += 1
                continue
            # exceed k frequency
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1
            r += 1
        return max_len

