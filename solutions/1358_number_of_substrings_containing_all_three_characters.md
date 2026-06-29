# 1358. Number of Substrings Containing All Three Characters

- **Difficulty:** Medium
- **Topic:** Sliding window

[LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

## Approach

Use a sliding window with two pointers `l` and `r`. Expand `r` until the window `s[l..r-1]` contains all three characters. At that point, every substring that starts at `l` and ends anywhere from `r-1` to `n-1` is also valid — that is `n - r + 1` substrings — so we add that count directly instead of enumerating each one. Then we shrink the window from the left by incrementing `l`, and repeat until the window is no longer valid, at which point we resume expanding `r`.

This works because extending a valid window to the right can only keep it valid, never invalidate it.

## Complexity

- **Time:** O(n) — each of the two pointers traverses the string at most once
- **Space:** O(1) — the frequency map holds at most 3 fixed keys

## Code

[View solution](../code/1358_number_of_substrings_containing_all_three_characters.py)
