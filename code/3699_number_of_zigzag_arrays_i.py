# Problem: Number of ZigZag Arrays I
# Topic: Dynamic programming
# Difficulty: Hard

'''
You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

Each element lies in the range [l, r].
No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.
Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).



Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

[4, 5, 4]
[5, 4, 5]

Constraints:

3 <= n <= 2000
1 <= l < r <= 2000
'''


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        dp_plus_pre_sum_array = []
        dp_minus_pre_sum_array = []
        MOD = 10 ** 9 + 7

        # do the same for each index i, and also fill the pre_sum array
        for i in range(n):
            temp_pre_sum_plus = [0]
            temp_pre_sum_minus = [0]
            for x in range(l, r + 1):
                if i == 0:
                    temp_pre_sum_plus.append((temp_pre_sum_plus[-1] + 1) % MOD)
                    temp_pre_sum_minus.append((temp_pre_sum_minus[-1] + 1) % MOD)
                else:
                    temp_pre_sum_plus.append((temp_pre_sum_plus[-1] + dp_minus_pre_sum_array[x - l]) % MOD)
                    temp_pre_sum_minus.append((temp_pre_sum_minus[-1] + (
                            dp_plus_pre_sum_array[r - l + 1] - dp_plus_pre_sum_array[x - l + 1]) % MOD) % MOD)
            dp_plus_pre_sum_array = temp_pre_sum_plus
            dp_minus_pre_sum_array = temp_pre_sum_minus

        return (dp_plus_pre_sum_array[-1] + dp_minus_pre_sum_array[-1]) % MOD


print(Solution().zigZagArrays(n=3, l=4, r=5))
