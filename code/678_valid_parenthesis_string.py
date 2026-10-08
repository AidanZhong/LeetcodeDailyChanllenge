# Problem: Valid Parenthesis String
# Topic: Dynammic programming
# Difficulty: Medium


class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        for i in s:
            if i == '(':
                lo += 1; hi += 1
            elif i == ')':
                lo -= 1; hi -= 1
            else:
                lo -= 1; hi += 1
            # check
            if hi < 0:
                return False
            lo = max(lo, 0)


        return lo == 0
