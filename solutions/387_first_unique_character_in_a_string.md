# 387. First Unique Character in a String

- **Difficulty:** Easy
- **Topic:** Hashset

[LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)

## Approach

Use a hashset to record the index of the character if we see it. To pop out the duplicated ones, we will use a set called $visited$, each time we meet a character we will check if it is in the set, if it is, we will pop it from the hashset. The remained ones are the Unique characters. We need to get the least index.

## Complexity

- **Time:** O(n log n) — the pass is O(n), but sorting the remaining unique entries is O(k log k) where k ≤ n (worst case O(n log n)). Note: this could be O(n) by just tracking the running min index instead of sorting.
- **Space:** O(k) where k is the number of distinct characters (bounded by alphabet size, so effectively O(1) for fixed alphabets like lowercase English letters).

## Code

[View solution](../code/387_first_unique_character_in_a_string.py)
