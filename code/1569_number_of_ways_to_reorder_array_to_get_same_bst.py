# Problem: Number of Ways to Reorder Array to Get Same BST
# Topic: BST
# Difficulty: Hard
import math


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def dfs(arr):
            root = arr[0]
            n = len(arr)
            left = []
            right = []
            for i in range(1, n):
                if arr[i] < root:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
            left_permutations = dfs(left) if left else 1
            right_permutations = dfs(right) if right else 1
            return (math.comb(n - 1, len(left)) * left_permutations * right_permutations)% (10 ** 9 + 7)
        return (dfs(nums) - 1) % (10 ** 9 + 7)


print(Solution().numOfWays([2, 1, 3]))  # Output: 1
