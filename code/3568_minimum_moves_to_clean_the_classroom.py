# Problem: Minimum Moves to Clean the Classroom
# Topic: Simulation
# Difficulty: Medium
from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        q = deque()
        # find the starting point
        n = len(classroom)
        m = len(classroom[0])
        start_point = -1, -1
        litter_index = {}
        for i in range(n):
            for j in range(m):
                if classroom[i][j] == 'S':
                    start_point = i, j
                elif classroom[i][j] == 'L':
                    litter_index[(i, j)] = len(litter_index)
        litter_count = len(litter_index)
        if litter_count == 0:
            return 0
        full_mask = (1 << litter_count) - 1

        sx, sy = start_point
        q.append((0, sx, sy, energy, 0))
        visited = {(sx, sy, energy, 0)}
        while q:
            moves, x, y, cur_energy, mask = q.popleft()
            if cur_energy == 0:
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and classroom[nx][ny] != 'X':
                    n_energy = energy if classroom[nx][ny] == 'R' else cur_energy - 1
                    n_mask = mask
                    if (nx, ny) in litter_index:
                        n_mask |= 1 << litter_index[(nx, ny)]
                    if n_mask == full_mask:
                        return moves + 1
                    state = (nx, ny, n_energy, n_mask)
                    if state not in visited:
                        visited.add(state)
                        q.append((moves + 1, nx, ny, n_energy, n_mask))
        return -1


# print(Solution().minMoves(["S.", "XL"], 2))
# print(Solution().minMoves(classroom=["LS", "RL"], energy=4))
print(Solution().minMoves(["SR"], 1))
