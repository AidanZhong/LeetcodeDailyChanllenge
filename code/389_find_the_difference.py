# Problem: Find the Difference
# Topic: Hash set
# Difficulty: Easy

from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_dict = defaultdict(int)
        for i in s:
            char_dict[i] += 1
        for i in t:
            char_dict[i] -= 1
            if char_dict[i] == 0:
                char_dict.pop(i)

        return char_dict.popitem()[0]
