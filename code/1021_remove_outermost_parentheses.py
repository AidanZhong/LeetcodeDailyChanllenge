# Problem: Remove Outermost Parentheses
# Topic: String
# Difficulty: Easy


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = 0
        ans = ''
        start = 0
        for i, c in enumerate(s):
            if c == '(':
                stack += 1
            else:
                stack -= 1
            if stack == 0:
                ans += s[start + 1:i]
                start = i + 1
        return ans

