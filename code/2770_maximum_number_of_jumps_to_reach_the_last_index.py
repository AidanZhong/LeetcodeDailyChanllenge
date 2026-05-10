# Problem: Maximum Number of Jumps to Reach the Last Index
# Topic: Dynamic Programming
# Difficulty: Medium
'''
You are given a 0-indexed array nums of n integers and an integer target.

You are initially positioned at index 0. In one step, you can jump from index i to any index j such that:

0 <= i < j < n
-target <= nums[j] - nums[i] <= target
Return the maximum number of jumps you can make to reach index n - 1.

If there is no way to reach index n - 1, return -1.
'''
from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        next_jump_dict = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    next_jump_dict[i].append(j)

        @cache
        def dp(i):
            '''
            :param i: current index
            :return: maximum jump to reach n - 1 from i, if it is impossible, return -1
            '''
            if i == n - 1:
                return 0
            maxi = 0
            for next_index in next_jump_dict[i]:
                maxi = max(maxi, dp(next_index) + 1)
            return maxi if maxi != 0 else -1

        return dp(0)


print(Solution().maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=2))
print(Solution().maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=3))
print(Solution().maximumJumps(nums=[1, 3, 6, 4, 1, 2], target=0))
print(Solution().maximumJumps(nums=[1, 0, 2], target=1))
