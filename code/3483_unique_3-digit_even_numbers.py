# Problem: Unique 3-Digit Even Numbers
# Topic: Math
# Difficulty: Easy
from collections import defaultdict
from itertools import permutations
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans_set = set()
        for perm in permutations(digits, 3):
            num = int(''.join(map(str, perm)))
            if 100 <= num <= 999 and num % 2 == 0:
                ans_set.add(num)
        return len(ans_set)
