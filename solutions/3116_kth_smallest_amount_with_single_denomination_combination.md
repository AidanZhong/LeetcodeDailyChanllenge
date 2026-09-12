# 3116. Kth Smallest Amount With Single Denomination Combination

- **Difficulty:** Hard
- **Topic:** Number Theory

[LeetCode](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/)

## Approach

Since coins can't be combined, the only amounts reachable using a given denomination
`coin` are its multiples: `coin, 2*coin, 3*coin, ...`. So the full set of reachable
amounts is the **union of the multiples of each coin** in the array. This means:

1. The reachable amounts, sorted, form a monotonically increasing sequence — so the
   k-th smallest can be found with **binary search on the answer** `x`, using a helper
   `count(x)` = "how many reachable amounts are ≤ x".
2. `count(x)` is a "size of union" problem, solved with **inclusion-exclusion** over
   all non-empty subsets of coins:
   - For each subset, compute `lcm` of its coins (multiples of the lcm = numbers
     divisible by every coin in the subset).
   - Add `x // lcm` if the subset size is odd, subtract if even, to avoid
     double-counting numbers divisible by multiple coins.
3. Binary search bounds: `l = k` (smallest possible k-th value, if `coins = [1]`),
   `r = coins[0] * k` (k-th multiple of the smallest coin alone is always a safe
   upper bound, since adding more coins only adds more reachable values, never removes any).
4. Inside `count(x)`, iterate `mask` from `1` to `2^n - 1` to represent every non-empty
   subset; use bit `i` of `mask` to check whether `coins[i]` is included, and break
   early once the running `lcm` exceeds `x` (that subset contributes 0 anyway).
5. Standard binary search: shrink `[l, r]` based on whether `count(mid) < k`.

## Complexity

- **Time:** `O(log(coins[0] * k) * 2^n * n)` — binary search runs
  `O(log(coins[0] * k))` iterations; each `count(x)` call loops over `2^n` subsets,
  and each subset does up to `O(n)` work to check bits and compute the running `lcm`.
- **Space:** `O(1)` extra space (excluding input array and sort's internal overhead).

## Code

File:/C:/Users/AidanZhong/PycharmProjects/LeetcodeDailyChanllenge/code/3116_kth_smallest_amount_with_single_denomination_combination.py

[View solution](../code/3116_kth_smallest_amount_with_single_denomination_combination.py)