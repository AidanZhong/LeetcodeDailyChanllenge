# Problem: Calculate Digit Sum of a String
# Topic: String simulation
# Difficulty: Easy


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def exec_round():
            # split
            groups = [s[i:i + k] for i in range(0, len(s), k)]
            # sum
            return ''.join(str(sum(int(c) for c in group)) for group in groups)

        while len(s) > k:
            s = exec_round()
        return s
