# Problem: Maximum Nesting Depth of the Parentheses
# Topic: Stack
# Difficulty: Easy


class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for i in s:
            if i == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif i == ')':
                depth -= 1
        return max_depth
