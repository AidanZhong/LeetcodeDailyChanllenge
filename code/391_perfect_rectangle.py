# Problem: Perfect Rectangle
# Topic: Geometry
# Difficulty: Hard
from collections import defaultdict
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        mini_x = min(rectangles, key=lambda x: x[0])[0]
        mini_y = min(rectangles, key=lambda x: x[1])[1]
        max_x = max(rectangles, key=lambda x: x[2])[2]
        max_y = max(rectangles, key=lambda x: x[3])[3]

        # corner count check
        def corner_check():
            corner_count = defaultdict(int)
            for x, y, a, b in rectangles:
                corner_count[(x, y)] += 1
                corner_count[(a, y)] += 1
                corner_count[(x, b)] += 1
                corner_count[(a, b)] += 1

            corner_count[(mini_x, mini_y)] += 1
            corner_count[(max_x, max_y)] += 1
            corner_count[(mini_x, max_y)] += 1
            corner_count[(max_x, mini_y)] += 1
            for k, v in corner_count.items():
                if v % 2 != 0:
                    return False
            return True

        def area_check():
            total_area = (max_x - mini_x) * (max_y - mini_y)
            for x, y, a, b in rectangles:
                total_area -= (a - x) * (b - y)
            return total_area == 0

        return corner_check() and area_check()
