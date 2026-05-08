# 3629. Minimum Jumps to Reach End via Prime Teleportation

- **Difficulty:** Medium
- **Topic:** BFS, SPF

## Approach

This is a shortest-path problem on an implicit graph where each array index is a node. From any index you can reach its two adjacent neighbors, or — if its value is prime `p` — teleport to any index whose value is divisible by `p`.

**Why naive BFS is O(n²):** For every prime-valued node dequeued, scanning all `n` elements to find teleportation targets costs O(n) per node, giving O(n²) overall.

**Key insight — invert the grouping:** Instead of "for each prime, scan all nums", precompute a `teleportation` map by doing the reverse: for each index `j`, factorize `nums[j]` and register `j` under each of its prime factors. Factorization is done efficiently using a **Smallest Prime Factor (SPF) sieve**, where `spf[x]` stores the smallest prime that divides `x`. Dividing out each prime with the inner `while x % prime == 0` loop ensures every prime factor is found in O(log MAX) per number.

During BFS, when standing on a prime `p`, look up `teleportation[p]` directly instead of scanning the array. After consuming the group, **delete** it from the map — BFS guarantees the first visit is already the shortest, so this group will never need to be revisited.

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
