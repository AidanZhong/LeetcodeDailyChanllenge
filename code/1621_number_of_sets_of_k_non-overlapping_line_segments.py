# Problem: Number of Sets of K Non-Overlapping Line Segments
# Topic: Dynamic programming
# Difficulty: Medium
from collections import defaultdict
from functools import cache


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(i, j):
            # the [0~i] point, the number of sets of j non-overlapping line segments
            if j == 0:
                return 1
            if i < j:
                return 0

            ans = dp(i - 1, j) + pre(i - 1, j - 1)

            return ans % MOD

        @cache
        def pre(i, j):
            # dp(0, j) + dp(1, j) + ... + dp(i, j)
            if i < j:
                return 0
            return (pre(i - 1, j) + dp(i, j)) % MOD

        # warm the cache bottom-up so the recursion never goes deep
        # only i - j <= n - 1 - k can reach dp(n - 1, k)
        for j in range(k + 1):
            for i in range(j, j + n - k):
                dp(i, j)

        return dp(n - 1, k)


print(Solution().numberOfSets(4, 2))
