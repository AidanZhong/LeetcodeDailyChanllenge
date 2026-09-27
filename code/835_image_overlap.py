# Problem: Image Overlap
# Topic: Matrix
# Difficulty: Medium
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        delta = (0, 0)
        n = len(img1)

        def cal_overlap():
            overlap = 0
            for i in range(n):
                for j in range(n):
                    new_x, new_y = i + delta[0], j + delta[1]
                    if 0 <= new_x < n and 0 <= new_y < n:
                        if img1[i][j] == 1 and img2[i + delta[0]][j + delta[1]] == 1:
                            overlap += 1
            return overlap

        max_overlap = cal_overlap()
        for x in range(-n + 1, n):
            for y in range(-n + 1, n):
                delta = (x, y)
                max_overlap = max(max_overlap, cal_overlap())
                print(delta, cal_overlap())
        return max_overlap


print(Solution().largestOverlap([[0, 1], [1, 1]], [[1, 1], [1, 0]]))
