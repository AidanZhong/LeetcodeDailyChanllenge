# Problem: Concatenate Non-Zero Digits and Multiply by Sum I
# Topic: Math
# Difficulty: Easy


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        l = []
        s = 0
        for i in str(n):
            if i != '0':
                l.append(i)
                s += int(i)
        return int(''.join(l)) * s
