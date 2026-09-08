# Problem: Count Commas in Range
# Topic: Math
# Difficulty: Easy


class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        multiplier = 1
        while n >= 1000:
            left = n - 999
            count += multiplier * left
            n //= 1000
            multiplier += 1
        return count
