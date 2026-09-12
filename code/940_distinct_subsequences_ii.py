# Problem: Distinct Subsequences II
# Topic: Dynamic programming
# Difficulty: Hard


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1 # empty string
        last_occurrence = {}
        for i in range(1, len(s) + 1):
            cur_char = s[i - 1]
            dp[i] = (2 * dp[i - 1]) % (10**9 + 7)

            if cur_char in last_occurrence:
                dp[i] -= dp[last_occurrence[cur_char]]

            last_occurrence[cur_char] = i - 1

        return (dp[len(s)] - 1) % (10**9 + 7)  # subtract the empty subsequence