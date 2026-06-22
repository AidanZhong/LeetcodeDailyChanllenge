# 3969. Valid Subarrays With Matching Sum Digits I

- **Difficulty:** medium
- **Topic:** pre sum

## Approach

Use `preSum` to fast calculate the sum of any consecutive subarray. And check the first and last digit of the sum.

## Complexity

- **Time:** O(n²) — nested loops over all subarrays; prefix sum lookup is O(1) per pair
- **Space:** O(n) — prefix sum array of length n+1

## Code

[View solution](../code/3969_valid_subarrays_with_matching_sum_digits_i.py)
