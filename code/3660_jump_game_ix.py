# Problem: Jump Game IX
# Topic: DSU
# Difficulty: Medium

'''
You are given an integer array nums.

From any index i, you can jump to another index j under the following rules:

Jump to index j where j > i is allowed only if nums[j] < nums[i].
Jump to index j where j < i is allowed only if nums[j] > nums[i].
For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.

Return an array ans where ans[i] is the maximum value reachable starting from index i.
'''
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.size: list[int] = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dsu = DSU(n)
        stack = [] # min stack

        for i in range(n - 1, -1, -1):
            v = nums[i]
            cur_min = v

            while stack and stack[-1][1] < v:
                rep, min_val = stack.pop()
                dsu.union(i, rep)
                cur_min = min(cur_min, min_val)

            stack.append((dsu.find(i), cur_min))

        comp_max = {}
        for i in range(n):
            p = dsu.find(i)
            if nums[i] > comp_max.get(p, 0):
                comp_max[p] = nums[i]

        return [comp_max[dsu.find(i)] for i in range(n)]


print(Solution().maxValue(nums=[2, 1, 3]))
print(Solution().maxValue(nums=[2, 3, 1]))
