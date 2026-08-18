# Problem: Stone Game V
# Topic: dynamic programming
# Difficulty: Hard
from functools import cache
from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        @cache
        def dp(l, r):
            # max value alice can get from stoneValue[l:r]
            if l == r:
                # boarder case, only 1 stone left
                return 0
            ans = left_sum = 0
            total = sum(stoneValue[l: r + 1])
            for x in range(l, r):
                # try to split at position x
                left_sum += stoneValue[x]
                right_sum = total - left_sum
                if left_sum > right_sum:
                    # bob will throw left part
                    ans = max(ans, right_sum + dp(x + 1, r))
                elif left_sum < right_sum:
                    # bob will throw right part
                    ans = max(ans, left_sum + dp(l, x))
                else:
                    # bob will throw either part
                    ans = max(ans, left_sum + dp(l, x), right_sum + dp(x + 1, r))
            return ans

        return dp(0, len(stoneValue) - 1)
