# 2770. Maximum Number of Jumps to Reach the Last Index

- **Difficulty:** Medium
- **Topic:** Dynamic Programming

https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/

## Approach

This is a classic dynamic programming problem.
First, we need a dictionary (Hashmap) to store the possible jump index for each index.

Then, we define the dp function to which dp(i) means the maximum number of jumps to reach the index n - 1 from index i.
If it is impossible return -1.

## Complexity

- **Time:** O(n²)
  - Building `next_jump_dict`: O(n²) — all pairs (i, j) are checked
  - DP evaluation: O(n²) — each of the n states is computed once; total transitions across all states is bounded by the number of edges, O(n²)
- **Space:** O(n²)
  - `next_jump_dict` stores up to O(n²) edges in the worst case
  - Memoization cache and recursion stack: O(n)

## Code

[View solution](../code/2770_maximum_number_of_jumps_to_reach_the_last_index.py)
