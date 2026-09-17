# Problem: Find Two Non-overlapping Sub-arrays Each With Target Sum
# Topic: Sliding window, Prefix sum
# Difficulty: Medium
import sys
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pre_sum = [0]
        for x in arr:
            pre_sum.append(pre_sum[-1] + x)

        n = len(arr)
        l, r = 0, 0

        best = [sys.maxsize] * n
        ans = sys.maxsize
        while l <= r < n:
            if r > 0:
                best[r] = min(best[r], best[r - 1])
            if pre_sum[r + 1] - pre_sum[l] < target:
                r += 1
            elif pre_sum[r + 1] - pre_sum[l] > target:
                l += 1
                if l > r:
                    r = l
            else:
                best[r] = min(best[r], r - l + 1)
                if l > 0 and best[l - 1] != sys.maxsize:
                    ans = min(ans, best[l - 1] + r - l + 1)
                r += 1
                l += 1

        return ans if ans != sys.maxsize else -1


print(Solution().minSumOfLengths([3, 2, 2, 4, 3], 3))
