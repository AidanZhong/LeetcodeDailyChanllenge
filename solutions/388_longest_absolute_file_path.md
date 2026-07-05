# 388. Longest Absolute File Path

- **Difficulty:** Medium
- **Topic:** DFS

[LeetCode](https://leetcode.com/problems/longest-absolute-file-path/)

## Approach

Firstly, split the input by \n. 

For each line, the number of \t is the depth of directory. The followed up is the actual name. So for each line we need to know the length of the parent directory. So we use an array to record the length of each stack.

## Complexity

- **Time:**  O(n) where n is the total length of the input string (each line processed once, with O(depth) work for counting tabs — bounded by line length).
- **Space:** O(n) worst case for the stacks array (proportional to max depth, which is bounded by number of lines) plus the split lines list.

## Code

[View solution](../code/388_longest_absolute_file_path.py)
