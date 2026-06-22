# Problem: Maximum Total Value
# Topic: binary search
# Difficulty: Hard

'''
You are given two integer arrays value and decay, and an integer m.

value[i] represents the initial value at index i.
decay[i] represents how much the value decreases after each selection of index i.
You may select any index multiple times. The total number of selections across all indices must not exceed m.

If you select index i for the tth time, where t is 1-indexed, the value gained is value[i] - decay[i] * (t - 1).

Return the maximum total value you can obtain. Since the answer may be large, return it modulo 109 + 7.



Example 1:

Input: value = [6,5,4], decay = [2,1,1], m = 4

Output: 19

Explanation:

One optimal sequence of selections is as follows:

By selecting index 0, the value gained is 6.
By selecting index 1, the value gained is 5.
By selecting index 2, the value gained is 4.
By selecting index 0 again, the value gained is 6 - 2 = 4.
The total value is 6 + 5 + 4 + 4 = 19. No other sequence of at most 4 selections gives a higher total value.
'''

class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = 10**9 + 7
        n = len(value)

        def get_count_and_value(W):
            # taking all value >= W, fill the rest with W
            total_count, total_value = 0, 0
            for i in range(n):
                if value[i] >= W:
                    t = (value[i] - W) // decay[i] + 1
                    total_count += t
                    total_value += t * value[i] - decay[i] * t * (t - 1) // 2
            return total_count, total_value

        count1, value1 = get_count_and_value(1)
        if count1 <= m:
            return value1 % MOD

        # bin search W
        left, right = 1, max(value)
        while left < right:
            mid = (left + right + 1) // 2
            count_mid, value_mid = get_count_and_value(mid)
            if count_mid < m:
                # could get more, so W should be smaller
                right = mid - 1
            else:
                left = mid

        W = left
        count_W, value_W = get_count_and_value(W + 1)
        remaining = m - count_W
        return (value_W + remaining * W) % MOD