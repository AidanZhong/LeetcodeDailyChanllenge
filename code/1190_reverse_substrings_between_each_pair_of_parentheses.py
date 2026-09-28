# Problem: Reverse Substrings Between Each Pair of Parentheses
# Topic: Array
# Difficulty: Medium


class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)

        def dfs(idx):
            current = ''
            while idx in range(n):
                if s[idx] == '(':
                    temp, idx = dfs(idx + 1)
                    current += temp[::-1]
                elif s[idx] == ')':
                    return current, idx
                else:
                    current += s[idx]
                idx += 1
            return current, idx

        return dfs(0)[0]

print(Solution().reverseParentheses("(abcd)"))