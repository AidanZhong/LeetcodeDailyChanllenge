# Problem: Minimum Sum of Squared Difference
# Topic: Greedy
# Difficulty: Medium
import heapq
from collections import deque
from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diffs = []
        for i in range(len(nums1)):
            heapq.heappush(diffs, -abs(nums1[i] - nums2[i]))
        k = k1 + k2
        if -sum(diffs) <= k:
            return 0
        ans = 0
        item = -heapq.heappop(diffs)  # current max value
        cnt = 1  # how many diffs are at this max value
        while k > 0:
            while diffs and -diffs[0] == item:
                heapq.heappop(diffs)
                cnt += 1
            nxt = -diffs[0] if diffs else 0
            if k >= cnt * (item - nxt):
                # lower the whole group down to the next value
                k -= cnt * (item - nxt)
                item = nxt
            else:
                # spread the remaining k over the group
                dec, rem = divmod(k, cnt)
                item -= dec
                k = 0
                ans += rem * (item - 1) ** 2 + (cnt - rem) * item ** 2
                cnt = 0
        ans += cnt * item * item
        for item in diffs:
            ans += item * item
        return ans
