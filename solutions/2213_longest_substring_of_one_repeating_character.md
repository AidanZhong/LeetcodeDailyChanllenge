# 2213. Longest Substring of One Repeating Character

- **Difficulty:** Hard
- **Topic:** Array

[LeetCode](https://leetcode.com/problems/longest-substring-of-one-repeating-character/)

## Approach

Maintain the string as runs of consecutive identical characters. Represent each run by its ending index and character (arr as list of (end_index, char)). Keep a multiset (SortedList) of run lengths for O(log n) insert/remove and O(1) access to the current maximum.

For each query (change character at index idx to c):
- If the character is already c, the answer is the current maximum run length.
- Otherwise, find the run containing idx using binary search on run end indices.
- Remove that run's length from the multiset and split it into up to three parts: left (before idx), the new single-character run at idx, and right (after idx). Insert lengths for any non-empty parts.
- Attempt to merge the new single-character run with adjacent runs that have the same character, updating the multiset and arr accordingly.
- Update the string character and append the current maximum length from the multiset to the answer list.

This preserves your original arr and bin_search_index structure while fixing missing run-length bookkeeping and handling duplicates with a SortedList.

## Complexity

- **Time:** O((n + m) log n) where n is the original string length and m is number of queries. Each query does binary search + O(log n) multiset ops and a small number of constant-time list manipulations and merges.
- **Space:** O(n) for the runs and multiset.

## Code

[View solution](../code/2213_longest_substring_of_one_repeating_character.py)
