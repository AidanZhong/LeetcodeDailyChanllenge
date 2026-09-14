# Problem: Rectangle Overlap
# Topic: Math
# Difficulty: Easy
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] > rec2[0]:
            rec1, rec2 = rec2, rec1
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        if x3 < x2 and y3 < y2 and y4 > y1:
            return True
        return False


print(Solution().isRectangleOverlap([0, 0, 1, 1], [0, 0, 1, 1]))  # Output: True
