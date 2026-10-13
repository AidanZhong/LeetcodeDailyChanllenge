# Problem: Maximum Alternating Sum of Squares
# Topic: Greedy
# Difficulty: Medium
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True, key=lambda x: x * x)
        n = len(nums)
        positive_half = n // 2 + n % 2
        ans = 0
        for i in range(n):
            if i < positive_half:
                ans += nums[i] * nums[i]
            else:
                ans -= nums[i] * nums[i]
        return ans


print(Solution().maxAlternatingSum([1, 2, 3]))
print(Solution().maxAlternatingSum([1, -1, 2, -2, 3, -3]))
