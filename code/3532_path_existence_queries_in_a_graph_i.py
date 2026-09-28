# Problem: Path Existence Queries in a Graph I
# Topic: DSU
# Difficulty: Medium
import sys
from typing import List


class DSU:
    def __init__(self, size):
        self.pa = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.pa[y] = x
        self.size[x] += self.size[y]

    def beautify(self):
        for i in range(len(self.pa)):
            self.pa[i] = self.find(i)


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        
