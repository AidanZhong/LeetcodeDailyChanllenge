# 3737. Count Subarrays With Majority Element I

- **Difficulty:** Medium
- **Topic:** prefix sum

[LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-i/)

## Approach

According to the problem statement, for each element, we only care if it is the target element or not.
So we reframe the array as a binary array, where 1 means the target element and 0 means not.

Then for each subarray of length `k`, we just need to check if its sum is strictly greater than `k / 2`. In integer arithmetic, this is equivalent to `sum > k // 2` — since `count` is an integer, `count > k/2` holds iff `count > floor(k/2)`.

For quick calculation of the sum of the subarray, we can use prefix sum.

We iterate over all O(n²) pairs `(l, r)` and apply the check in O(1) using the prefix sum.

## Complexity

- **Time:** O(n²) — two nested loops over all subarrays; acceptable given the small constraints.
- **Space:** O(n) — for the prefix sum array.

## Code

[View solution](../code/3737_count_subarrays_with_majority_element_i.py)
