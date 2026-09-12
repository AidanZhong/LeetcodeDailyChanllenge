# 3090. Maximum Length Substring With Two Occurrences

- **Difficulty:** Easy
- **Topic:** Sliding Window

[LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)

## Approach

Keep a sliding window `[l, r]` and a frequency dictionary of the characters inside it.

Expand the window by one character at a time. After adding `s[r]`, the only character that can break the
rule is `s[r]` itself, so while its count is greater than 2, shrink the window from the left (dropping
`s[l]` from the dictionary) until the window is valid again. Every time the window is valid, update the
answer with `r - l + 1`.

Since `l` only ever moves forward, each character enters and leaves the window at most once.

## Complexity

- **Time:** O(n) — each of `l` and `r` walks the string once.
- **Space:** O(1) — the frequency dictionary holds at most 26 lowercase letters.

## Code

[View solution](../code/3090_maximum_length_substring_with_two_occurrences.py)
