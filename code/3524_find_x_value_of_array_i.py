# Problem: Find X Value of Array I
# Topic: Dynamic programming
# Difficulty: Medium
from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * k

        def dp(i):
            # first i elements, return counts of subarrays ending at i - 1 by remainder
            if i == 0:
                return [0] * k
            current_remainder = nums[i - 1] % k
            previous_x_values = dp(i - 1)
            new_x_values = [0] * k
            new_x_values[current_remainder] = 1
            for r in range(k):
                new_remainder = (r * current_remainder) % k
                new_x_values[new_remainder] += previous_x_values[r]
            for r in range(k):
                result[r] += new_x_values[r]
            return new_x_values

        dp(n)
        return result


print(Solution().resultArray([1, 2, 3, 4, 5], 3))
print(Solution().resultArray([1, 2, 4, 8, 16, 32], 4))
print(Solution().resultArray([1], 1))
