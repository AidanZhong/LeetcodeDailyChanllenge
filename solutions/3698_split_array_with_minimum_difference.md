# 3698. Split Array With Minimum Difference


- **Difficulty:** Medium
- **Topic:** array

## Approach

For a split at index i (left = nums[0..i], right = nums[i+1..n-1]) to be valid, left must be strictly increasing and right must be strictly decreasing. This forces the array to be a "mountain": non-stop increasing up to some peak, then non-stop decreasing.

Here is the key insight: for any valid mountain, the elements before the peak are locked into left and the elements after the peak are locked into right. The only free choice is which side the peak itself belongs to. So there are exactly two candidate splits — peak in left, or peak in right — and we just pick the one with the smaller absolute difference.

The algorithm does a single left-to-right pass:
1. Accumulate elements into left while the sequence is strictly increasing.
2. When the sequence starts decreasing, record the peak and accumulate remaining elements into right. If the sequence ever increases again after it has started decreasing, no valid split exists — return -1.
3. At the end, compute both candidate splits and return the minimum absolute difference.

One edge case: if the array is entirely increasing, the last element acts as the peak — the only valid split is all-but-last in left and the last element alone in right.

## Complexity

- **Time:** O(n) — single pass through the array
- **Space:** O(1) — only a handful of running sums

## Code

[View solution](../code/3698_split_array_with_minimum_difference.py)
