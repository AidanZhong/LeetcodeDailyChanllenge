# Problem: Maximum Number of Non-overlapping Palindrome Substrings
# Topic: Dynamic Programming
# Difficulty: Hard
from functools import cache


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        @cache
        def dp(i):
            # s[:i]. The most palindromes we can get from s[:i]
            if i < k:
                return 0
            if is_palindrome(i - k, i - 1):
                return max(dp(i - k) + 1, dp(i - 1))
            if is_palindrome(i - k - 1, i - 1):
                return max(dp(i - k - 1) + 1, dp(i - 1))
            return dp(i - 1)

        return dp(n)
