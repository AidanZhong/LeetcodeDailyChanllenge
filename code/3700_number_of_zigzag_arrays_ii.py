# Problem: Number of ZigZag Arrays II
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

3 <= n <= 10^9
1 <= l < r <= 75
'''
import numpy as np


def matrix_power(M, n, mod):
    size = M.shape[0]
    result = np.eye(size, dtype=object)
    base = M.copy()
    while n > 0:
        if n & 1:
            result = result @ base % mod
        base = base @ base % mod
        n >>= 1
    return result


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        # constructing matrix M
        m = r - l + 1
        L = np.tril(np.ones((m, m), dtype=object), k=-1)  # lower triangle without diagonal
        U = np.triu(np.ones((m, m), dtype=object), k=1)  # upper triangle without diagonal
        zero = np.zeros((m, m), dtype=object)
        M = np.block([[zero, L],
                      [U, zero]])
        V_0 = np.ones((2 * m, 1), dtype=object)
        M_n = matrix_power(M, n - 1, MOD)
        V_n = M_n @ V_0 % MOD
        return int(np.sum(V_n)) % MOD


print(Solution().zigZagArrays(3, 4, 5))
