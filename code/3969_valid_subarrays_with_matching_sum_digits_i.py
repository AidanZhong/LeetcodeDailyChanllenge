# Problem: Valid Subarrays With Matching Sum Digits I
# Topic: pre sum
# Difficulty: medium

'''
You are given an integer array nums and an integer digit x.

A subarray nums[l..r] is considered valid if the sum of its elements satisfies both of the following conditions:

The first digit of the sum is equal to x.
The last digit of the sum is equal to x.
Return the number of valid subarrays.



Example 1:

Input: nums = [1,100,1], x = 1

Output: 4

Explanation:

The valid subarrays are:

nums[0..0]: sum = 1
nums[0..1]: sum = 1 + 100 = 101
nums[1..2]: sum = 100 + 1 = 101
nums[2..2]: sum = 1
Thus, the answer is 4.
'''


class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = nums.__len__()
        pre_sum = [0]
        for i in nums:
            pre_sum.append(pre_sum[-1] + i)

        count = 0
        for start in range(n):
            for end in range(start + 1, n + 1):
                sub_sum = pre_sum[end] - pre_sum[start]
                if int(str(sub_sum)[0]) == x and int(str(sub_sum)[-1]) == x:
                    count += 1
        return count