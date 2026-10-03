# Problem: Maximum Nesting Depth of Two Valid Parentheses Strings
# Topic: Stack
# Difficulty: Medium


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # keep stack1 higher depth than stack2, so that the maximum depth of both stacks is minimized
        stack1 = 0
        stack2 = 0
        ans = []
        for i in seq:
            if i == '(':
                if stack1 <= stack2:
                    stack1 += 1
                    ans.append(0)
                else:
                    stack2 += 1
                    ans.append(1)
            elif i == ')':
                if stack1 > stack2:
                    stack1 -= 1
                    ans.append(0)
                else:
                    stack2 -= 1
                    ans.append(1)
        return ans


