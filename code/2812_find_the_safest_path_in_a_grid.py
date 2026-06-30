# Problem: Find the Safest Path in a Grid
# Topic: BFS, binary search
# Difficulty: Medium

'''
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

Constraints:

1 <= grid.length == n <= 400
grid[i].length == n
grid[i][j] is either 0 or 1.
There is at least one thief in the grid.
'''
from collections import deque
from functools import cache
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = set()
        thieves = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    thieves.append((0, i, j))
                    visited.add((i, j))

        # init the safeness matrix
        safeness_matrix = [[-1] * n for _ in range(n)]
        q = deque(thieves)
        while q:
            safeness, x, y = q.popleft()
            safeness_matrix[x][y] = safeness
            # check all adjacent cells
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((safeness + 1, nx, ny))

        @cache
        def check_path_existence_by_limited_safeness(limit):
            q_in = deque([(0, 0)])
            if safeness_matrix[0][0] < limit or safeness_matrix[n - 1][n - 1] < limit:
                return False
            visited_in = set()
            visited_in.add((0, 0))
            while q_in:
                x, y = q_in.popleft()
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and safeness_matrix[nx][ny] >= limit and (nx, ny) not in visited_in:
                        q_in.append((nx, ny))
                        visited_in.add((nx, ny))
            return False

        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if check_path_existence_by_limited_safeness(mid):  # we could probably find bigger safeness factor
                if check_path_existence_by_limited_safeness(mid + 1):
                    l = mid + 1
                else:
                    return mid
            else:
                r = mid - 1
        return l


# print(Solution().maximumSafenessFactor(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
# print(Solution().maximumSafenessFactor(grid=[[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
# print(Solution().maximumSafenessFactor(grid=[[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]))
print(Solution().maximumSafenessFactor(grid=[[0, 1, 1], [0, 1, 1], [1, 1, 0]]))
