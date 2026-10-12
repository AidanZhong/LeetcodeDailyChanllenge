# Problem: Minimum Insertions to Balance a Parentheses String
# Topic: Greedy
# Difficulty: Medium


class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        stack = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack += 1
            else:
                if stack <= 0:
                    ans += 1  # add a (
                    stack += 1
                if i + 1 < len(s) and s[i + 1] == ')':
                    stack -= 1
                    i += 1
                else:
                    stack -= 1
                    ans += 1  # add a )
            i += 1
        ans += stack * 2  # add a ) for each (
        return ans


print(Solution().minInsertions("()()()()()("))
