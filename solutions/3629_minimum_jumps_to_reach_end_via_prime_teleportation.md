# 3629. Minimum Jumps to Reach End via Prime Teleportation

- **Difficulty:** Medium
- **Topic:** BFS, SPF

[LeetCode](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/)

## Approach

The problem is a graph traversal problem. Each index of array is a node. You start from the first index to move to the
last one. And you can move to any index whose value is divisible by the prime value at the current index, or an adjacent index.

So we can use BFS to find the shortest path. But during the BFS, we need to find the accessible nodes efficiently.
There are 2 adjacent nodes for each node. And if the node's value is a prime number, we need to find the "Prime teleportation"
positions.
If we use brute force, its time complexity is O(n²) which will exceed the time limit.

So we need a dictionary (i.e., a map from prime → set of indices) to store the accessible nodes for each prime number. And once the "Teleportation"
is visited, we need to remove the "Teleportation" from the dictionary. (Since if BFS visits the node again, the new step
will be no less than the previous visit.) The approach is: while traversing the array, we need to factorize each number and
put it into the prime teleportation dictionary using SPF (Smallest Prime Factor). SPF allows factorizing each number in O(log M)
by repeatedly dividing by `spf[x]` until `x` reaches 1, instead of O(√M) trial division.

## Complexity

- **Time:** O(M log log M + n log M), where M = max(nums) ≤ 10⁶ and n ≤ 10⁵
  - SPF sieve: O(M log log M) ≈ O(4 × 10⁶)
  - Building `teleportation` map: O(n log M) — each number factorized in O(log M) via SPF
  - BFS: O(n) — each index is enqueued at most once; each prime group is deleted after first use
- **Space:** O(M + n)
  - SPF array: O(M)
  - `teleportation` map + `visited` set + queue: O(n)

## Code

[View solution](../code/3629_minimum_jumps_to_reach_end_via_prime_teleportation.py)
