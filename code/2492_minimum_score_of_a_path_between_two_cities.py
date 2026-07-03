# Problem: Minimum Score of a Path Between Two Cities
# Topic: DSU
# Difficulty: Medium

'''
You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.


Example 1:


Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
Example 2:


Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.


Constraints:

2 <= n <= 105
1 <= roads.length <= 105
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 104
There are no repeated edges.
There is at least one path between 1 and n.
'''
import sys
from typing import List


class DSU:
    def __init__(self, size):
        self.pa = [i for i in range(size)]
        self.size = [1] * size
        self.score = [sys.maxsize] * size

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x, y, distance):
        x, y = self.find(x), self.find(y)
        if x == y:
            self.score[x] = min(self.score[x], self.score[y], distance)
            self.score[y] = min(self.score[x], self.score[y], distance)
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.pa[y] = x
        self.size[x] += self.size[y]
        self.score[x] = min(self.score[x], self.score[y], distance)
        self.score[y] = min(self.score[x], self.score[y], distance)

    def beautify(self):
        for i in range(len(self.pa)):
            pa = self.find(i)
            score = min(self.score[i], self.score[pa])
            self.score[i] = score
            self.score[pa] = score

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dsu = DSU(n)
        for x, y, distance in roads:
            dsu.union(x - 1, y - 1, distance)
        dsu.beautify()
        return dsu.score[0] if dsu.is_connected(0, n - 1) else -1
