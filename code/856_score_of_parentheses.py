# Problem: Score of Parentheses
# Topic: stack
# Difficulty: Medium


class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        def dfs(i):
            if i >= len(s) or s[i] == ')':
                return 0
            if s[i] == '(':
                if i + 1 < len(s) and s[i + 1] == ')':
                    return 1 + dfs(i + 2)
                # find the matching ')'
                stack, x = 0, i
                while True:
                    stack += 1 if s[x] == '(' else -1
                    if stack == 0:
                        break
                    x += 1
                return 2 * dfs(i + 1) + dfs(x + 1)

        return dfs(0)


# print(Solution().scoreOfParentheses(s="()"))
# print(Solution().scoreOfParentheses(s="(())"))
# print(Solution().scoreOfParentheses(s="()()"))
print(Solution().scoreOfParentheses("(())()"))
