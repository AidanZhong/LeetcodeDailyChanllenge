# Problem: Stone Game VIII
# Topic: Dynamic programming
# Difficulty: Hard
from functools import cache
from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix_sum = [0] * n
        prefix_sum[0] = stones[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + stones[i]

        @cache
        def dp(i):
            # maxi score diff we can get if current player is able to select from [i, n)
            if i == n - 1:
                return prefix_sum[i]
            return max(dp(i + 1), prefix_sum[i] - dp(i + 1))

        return dp(1)
