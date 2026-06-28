# Problem: Number of Strings That Appear as Substrings in Word
# Topic: String
# Difficulty: Easy


'''
Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.
'''
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for pattern in patterns:
            if pattern in word:
                ans += 1
        return ans
