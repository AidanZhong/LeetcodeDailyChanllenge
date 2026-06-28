# 1846. Maximum Element After Decreasing and Rearranging

- **Difficulty:** Medium
- **Topic:** Greedy

[LeetCode](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/)

## Approach

Sort the array first, then try to add one while traverse the array. Only add one if the current element is greater than
the previous element. Return the last element.

## Complexity

- **Time:** O(nlogn)
- **Space:** O(1)

## Code

[View solution](../code/1846_maximum_element_after_decreasing_and_rearranging.py)
