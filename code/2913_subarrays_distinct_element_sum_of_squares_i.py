# Problem: Subarrays Distinct Element Sum of Squares I
# Topic: Brutal Force
# Difficulty: Easy
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                count += pow(len(set(nums[i:j])), 2)
        return count


print(Solution().sumCounts(nums=[1, 2, 1]))
