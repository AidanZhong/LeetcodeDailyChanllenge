# Problem: Maximum Length Substring With Two Occurrences
# Topic: Sliding Window
# Difficulty: Easy
from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_count = defaultdict(int)
        l, r = 0, 0
        max_len = 0
        while l <= r < len(s):
            char_count[s[r]] += 1
            if char_count[s[r]] <= 2:
                max_len = max(max_len, r - l + 1)
                r += 1
                continue
            while char_count[s[r]] > 2:
                char_count[s[l]] -= 1
                l += 1
            r += 1
        return max_len


print(Solution().maximumLengthSubstring("bcbbbd"))
