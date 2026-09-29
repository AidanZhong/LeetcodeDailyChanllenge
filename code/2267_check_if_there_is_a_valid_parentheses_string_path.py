# Problem: Check if There Is a Valid Parentheses String Path
# Topic: Dynammic programming
# Difficulty: Hard
from collections import deque
from functools import cache


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        if grid[0][0] != '(':
            return False
        n = len(grid)
        m = len(grid[0])

        @cache
        def dp(i, j):
            if i == 0 and j == 0:
                return {1}

            # it goes from top cell
            ans = set()
            if i > 0:
                ans = ans.union(dp(i - 1, j))
            # it goes from left cell
            if j > 0:
                ans = ans.union(dp(i, j - 1))
            if grid[i][j] == '(':
                ans = {x + 1 for x in ans}
            elif grid[i][j] == ')':
                ans = {x - 1 for x in ans if x > 0}
            return ans

        return 0 in dp(n - 1, m - 1)
