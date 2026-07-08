# Problem: Concatenate Non-Zero Digits and Multiply by Sum II
# Topic: Prefix Sum, Math
# Difficulty: Medium
from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        pre_sum = [0]
        non_zero_count = [0]
        formed_number = [0]
        for i in s:
            pre_sum.append(pre_sum[-1] + int(i))
            if i != '0':
                non_zero_count.append(non_zero_count[-1] + 1)
                formed_number.append((formed_number[-1] * 10 + int(i)) % MOD)
            else:
                non_zero_count.append(non_zero_count[-1])
        non_zero_count = non_zero_count[1:]
        formed_number = formed_number[1:]

        if not formed_number:
            return [0] * len(queries)

        ans = []

        for l, r in queries:
            sum_q = pre_sum[r + 1] - pre_sum[l]
            a = non_zero_count[l - 1] if l != 0 else 0
            b = non_zero_count[r] - 1
            if a == 0:
                x = formed_number[b]
            else:
                x = (formed_number[b] - formed_number[a - 1] * pow(10, b - a + 1, MOD)) % MOD
            ans.append((sum_q * x) % MOD)
        return ans


# print(Solution().sumAndMultiply("10203004", [[0, 7], [1, 3], [4, 6]]))
print(Solution().sumAndMultiply("0", [[0, 0]]))
# print(Solution().sumAndMultiply("1000", [[0, 3], [1, 1]]))
