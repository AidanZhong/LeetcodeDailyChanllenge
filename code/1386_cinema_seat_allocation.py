# Problem: Cinema Seat Allocation
# Topic: Greedy
# Difficulty: Medium
from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        for row, col in reservedSeats:
            reserved[row].add(col)
        ans = 2 * (n - len(reserved))
        for cols in reserved.values():
            available_seats = [1, 1, 1]
            if 2 in cols or 3 in cols:
                available_seats[0] = 0
            if 4 in cols or 5 in cols:
                available_seats[0] = 0
                available_seats[1] = 0
            if 6 in cols or 7 in cols:
                available_seats[1] = 0
                available_seats[2] = 0
            if 8 in cols or 9 in cols:
                available_seats[2] = 0

            s = sum(available_seats)
            if s == 1 or s == 0:
                ans += s
            elif available_seats == [1, 1, 0] or available_seats == [0, 1, 1]:
                ans += 1
            else:
                ans += 2
        return ans



print(Solution().maxNumberOfFamilies(4, [[4, 3], [1, 4], [4, 6], [1, 7]]))
