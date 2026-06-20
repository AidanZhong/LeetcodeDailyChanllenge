# Problem: maximum building height
# Topic: math
# Difficulty: hard

'''
You want to build n new buildings in a city. The new buildings will be built in a line and are labeled from 1 to n.

However, there are city restrictions on the heights of the new buildings:

The height of each building must be a non-negative integer.
The height of the first building must be 0.
The height difference between any two adjacent buildings cannot exceed 1.
Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi, maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.

It is guaranteed that each building will appear at most once in restrictions, and building 1 will not be in restrictions.

Return the maximum possible height of the tallest building.


'''
from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort(key=lambda x: x[0])
        restrictions = [[1, 0]] + restrictions
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
        highest_buildings = []

        def f(i1, c1, i2, c2):
            '''
            return the maximum height of the tallest building among the buildings from i1 to i2
            '''
            if abs(i1 - i2) <= abs(c1 - c2):
                return min(c1, c2) + abs(i1 - i2)
            # inside is up then down
            l = i1 + (c2 - c1)
            r = i2
            mid = (l + r) // 2
            return c1 + (mid - i1)

        i0, c0 = restrictions[0]
        for idx in range(1, len(restrictions)):
            i, c = restrictions[idx]
            c = min(c, c0 + (i - i0))
            restrictions[idx] = [i, c]
            highest_buildings.append(f(i0, c0, i, c))
            i0, c0 = i, c

        # going right to left
        i0, c0 = restrictions[-1]
        for idx in range(len(restrictions) - 2, -1, -1):
            i, c = restrictions[idx]
            c = min(c, c0 + (i0 - i))
            restrictions[idx] = [i, c]
            highest_buildings[idx] = min(highest_buildings[idx], f(i, c, i0, c0))
            i0, c0 = i, c

        return max(highest_buildings)


# print(Solution().maxBuilding(n=5, restrictions=[[2, 1], [4, 1]]))
# print(Solution().maxBuilding(n=10,
#                              restrictions=[[8, 5], [9, 0], [6, 2], [4, 0], [3, 2], [10, 0], [5, 3], [7, 3], [2, 4]]))
print(Solution().maxBuilding(10, [[6, 0], [5, 2], [7, 0], [9, 1], [2, 4], [3, 4], [4, 0], [8, 2], [10, 0]]))
# print(Solution().maxBuilding(10, [[5, 3], [2, 5], [7, 4], [10, 3]]))
