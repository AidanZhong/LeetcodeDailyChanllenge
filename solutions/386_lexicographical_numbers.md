# 386. Lexicographical Numbers

- **Difficulty:** Medium
- **Topic:** DFS

[LeetCode](https://leetcode.com/problems/lexicographical-numbers/)

## Approach

The numbers are as a 10-ary tree. For example node $1$ has children $10, 11, 12, ...$. So a DFS from number $1$ visits all the numbers in exactly lex order.

In dfs(i), if i > n, stop, otherwise try to add a 0 to the end (goes for children), then try to plus one (goes for other siblings). So that we can traverse all the number less than n.

## Complexity

- **Time:** each number 1..n is visited/appended once.
- **Space:** O(log n) recursion depth (~ digit count of n), plus O(n) for the output list.

## Code

[View solution](../code/386_lexicographical_numbers.py)
