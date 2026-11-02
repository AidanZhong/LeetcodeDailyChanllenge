# Problem: Twisted Mirror Path Count
# Topic: Dynamic programming
# Difficulty: Medium
from functools import cache
from typing import List


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        MOD = 10**9 + 7

        @cache
        def dfs(i, j, come_from) -> int:
            # try to go right or down
            if i == n - 1 and j == m - 1:
                return 1

            if i < 0 or i >= n or j < 0 or j >= m:
                return 0

            if grid[i][j] == 1: # i am a mirror
                if come_from == "right":
                    # came from right, so go down
                    return dfs(i + 1, j, "down") % MOD
                elif come_from == "down":
                    # came from down, so go right
                    return dfs(i, j + 1, "right") % MOD

            # move right
            right = 0
            if j + 1 < m:
                if grid[i][j + 1] == 0:
                    right = dfs(i, j + 1, "right")
                else:  # a mirror, go down
                    right = dfs(i + 1, j + 1, "down")
            # move down
            down = 0
            if i + 1 < n:
                if grid[i + 1][j] == 0:
                    down = dfs(i + 1, j, "down")
                else:  # a mirror, go right
                    down = dfs(i + 1, j + 1, "right")
            # print(f"dfs({i}, {j}) = right: {right}, down: {down}")
            return (right + down) % MOD

        return dfs(0, 0, "right") % MOD


print(Solution().uniquePaths([[0, 1, 1], [1, 1, 0]]))  # Output: 1
