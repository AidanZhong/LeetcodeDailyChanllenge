# Problem: Split Array With Minimum Difference

# Topic: array
# Difficulty: Medium

'''
ou are given an integer array nums.

Split the array into exactly two subarrays, left and right, such that left is strictly increasing and right is strictly decreasing.

Return the minimum possible absolute difference between the sums of left and right. If no valid split exists, return -1.



Example 1:

Input: nums = [1,3,2]

Output: 2

Explanation:

i	left	right	Validity	left sum	right sum	Absolute difference
0	[1]	[3, 2]	Yes	1	5	|1 - 5| = 4
1	[1, 3]	[2]	Yes	4	2	|4 - 2| = 2
Thus, the minimum absolute difference is 2.
'''
from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        left = nums[0]
        right = 0
        prev = nums[0]
        n = len(nums)
        flag_of_going_up = True
        peak = 0
        for i in range(1, n):
            if flag_of_going_up:
                if nums[i] == prev:
                    flag_of_going_up = False
                    right += nums[i]
                if nums[i] < prev:
                    flag_of_going_up = False
                    right += nums[i]
                    peak = prev
                    prev = nums[i]
                    continue
                if nums[i] > prev:
                    left += nums[i]
                    prev = nums[i]
            else:
                if nums[i] >= prev:
                    return -1
                right += nums[i]
                prev = nums[i]
        if flag_of_going_up:
            left -= nums[-1]
            right += nums[-1]
        left -= peak
        # if peak on left:
        peak_l = abs(left + peak - right)
        # if peak on right:
        peak_r = abs(left - peak - right)

        return min(peak_l, peak_r)


# print(Solution().splitArray([1, 3, 2]))
print(Solution().splitArray([2, 4]))
