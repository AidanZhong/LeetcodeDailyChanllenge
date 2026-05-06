# Problem: Rotating the Box
# Topic: Matrix
# Difficulty: Medium

'''
You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.
'''

from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for line in boxGrid:
            line.append("*")
        m, n = len(boxGrid), len(boxGrid[0])
        count = 0
        for line in boxGrid:
            for idx, item in enumerate(line):
                if item == "#":
                    count += 1
                    # empty the box
                    line[idx] = "."
                elif item == "*":
                    # go back and stack the stones
                    while count > 0:
                        line[idx - count] = "#"
                        count -= 1
        ans = []
        for i in range(n):
            line = []
            for j in range(m-1, -1, -1):
                line.append(boxGrid[j][i])
            ans.append(line)
        return ans[:-1]


# print(Solution().rotateTheBox(boxGrid=[["#", ".", "#"]]))
print(Solution().rotateTheBox(boxGrid=[["#", ".", "*", "."],
                                       ["#", "#", "*", "."]]))
