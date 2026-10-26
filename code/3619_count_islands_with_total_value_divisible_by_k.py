# Problem: Count Islands With Total Value Divisible by K
# Topic: BFS
# Difficulty: Medium
from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        visited = set()

        def bfs(i: int, j: int) -> int:
            queue = [(i, j)]
            visited.add((i, j))
            total_value = grid[i][j]
            while queue:
                x, y = queue.pop(0)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] > 0:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        total_value += grid[nx][ny]
            return total_value

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and (i, j) not in visited:
                    total_value = bfs(i, j)
                    if total_value % k == 0:
                        count += 1
        return count
