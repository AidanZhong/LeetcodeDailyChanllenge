# Problem: Count Subarrays With Majority Element I
# Topic: prefix sum
# Difficulty: Medium

'''
You are given an integer array nums and an integer target.

Return the number of subarrays of nums in which target is the majority element.

The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.



Example 1:

Input: nums = [1,2,2,3], target = 2

Output: 5

Explanation:

Valid subarrays with target = 2 as the majority element:

nums[1..1] = [2]
nums[2..2] = [2]
nums[1..2] = [2,2]
nums[0..2] = [1,2,2]
nums[1..3] = [2,2,3]
So there are 5 such subarrays.
'''
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        new_nums = [i == target for i in nums]
        pre_sum = [0]
        for i in new_nums:
            pre_sum.append(pre_sum[-1] + i)

        count = 0
        for l in range(n):
            for r in range(l, n):
                if pre_sum[r + 1] - pre_sum[l] > (r - l + 1) // 2:
                    count += 1
        return count


print(Solution().countMajoritySubarrays(nums=[1, 2, 2, 3], target=2))
