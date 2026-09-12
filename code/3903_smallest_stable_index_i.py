# Problem: Smallest Stable Index I
# Topic: Array
# Difficulty: Easy


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_i = [nums[0]]
        for i in range(1, n):
            max_i.append(max(max_i[-1], nums[i]))

        min_i = [nums[-1]]
        for i in range(n-2, -1, -1):
            min_i.append(min(min_i[-1], nums[i]))
        min_i.reverse()

        for i in range(n):
            if max_i[i] - min_i[i] <= k:
                return i
        return -1

print(Solution().firstStableIndex([3,2,1], 1))  # Output: