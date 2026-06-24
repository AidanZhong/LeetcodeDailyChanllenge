# 3697. Compute Decimal Representation

- **Difficulty:** Easy
- **Topic:** Math

## Approach

A base-10 component is simply a non-zero digit scaled by its place value. Looking at the decimal representation of n, each non-zero digit at position k (from the right, 0-indexed) gives exactly one component: digit × 10^k. Zeros contribute nothing since 0 × 10^k = 0.

The minimum number of components is just the number of non-zero digits — there is no way to merge two components living at different powers of ten without carrying, which would only create more components. So minimality is automatic: just read off the non-zero digits.

The algorithm: extract each digit from right to left using repeated mod and integer division, skip zeros, record digit × 10^count, then reverse at the end for descending order.

## Complexity

- **Time:** O(log n) — one iteration per digit
- **Space:** O(log n) — the output array holds at most one entry per digit

## Code

[View solution](../code/3697_compute_decimal_representation.py)
