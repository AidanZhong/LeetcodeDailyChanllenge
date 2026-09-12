# Problem: Count Commas in Range II
# Topic: Math
# Difficulty: Medium


class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        power = 1000
        while power <= n:
            count += n - power + 1
            power *= 1000
        return count
