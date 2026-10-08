# Problem: Longest Valid Parentheses
# Topic: Dynammic programming
# Difficulty: Hard
from functools import cache


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        @cache
        def dp(i):
            if i <= 0:
                return 0
            if s[i] == "(":
                return 0
            if s[i - 1] == "(":
                return dp(i - 2) + 2
            j  = i - dp(i - 1) - 1
            if j < 0 or s[j] != "(":
                return 0
            return dp(i - 1) + dp(i - 2 - dp(i - 1)) + 2

        ans = 0
        for i in range(len(s)):
            ans = max(ans, dp(i))
        return ans


print(Solution().longestValidParentheses(")()())"))
