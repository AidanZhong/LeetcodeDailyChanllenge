# Problem: Find the Largest Almost Missing Integer
# Topic: hash set
# Difficulty: Easy
from collections import defaultdict
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        appearance_count = defaultdict(int)

        # init the window
        char_count = defaultdict(int)
        for i in range(k):
            char_count[nums[i]] += 1
            if char_count[nums[i]] == 1:
                appearance_count[nums[i]] += 1

        # traverse the array
        for i in range(k, len(nums)):
            # remove the leftmost element from the window
            char_count[nums[i - k]] -= 1

            # all the other elements will increase 1 appearance count
            for num in char_count:
                if char_count[num] >= 1:
                    appearance_count[num] += 1

            # add the new element to the window
            char_count[nums[i]] += 1
            if char_count[nums[i]] == 1:
                appearance_count[nums[i]] += 1

        # find the largest almost missing integer
        sorted_a_c = sorted(appearance_count.items(), key=lambda x: x[0], reverse=True)
        sorted_a_c.sort(key=lambda x: x[1])
        if sorted_a_c and sorted_a_c[0][1] == 1:
            return sorted_a_c[0][0]
        return -1


print(Solution().largestInteger(nums=[3, 9, 2, 1, 7], k=3))
