# 2958. Length of Longest Subarray With at Most K Frequency

- **Difficulty:** Medium
- **Topic:** Sliding window

[LeetCode](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/)

## Approach

Build a sliding window and maintain a frequency dictionary (Hash set). Whenever expanding,
check if the frequency of the last element is greater than k.

If it is, then shrink the window from the left until the frequency of the last element is less than or equal to k.
If it is not, update the maximum length of the window.

## Complexity

- **Time:** O(n) — both window pointers only move forward, so each element is added and removed at most once.
- **Space:** O(n) — the frequency dictionary holds at most one entry per distinct value.

## Code

[View solution](../code/2958_length_of_longest_subarray_with_at_most_k_frequency.py)
