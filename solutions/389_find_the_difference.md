# 389. Find the Difference

- **Difficulty:** Easy
- **Topic:** Hash set

[LeetCode](https://leetcode.com/problems/find-the-difference/)

## Approach

Use a hash set to store the number of appearances of each character in s, then subtract the number of appearances of
each character in t. The character left with value -1 is the answer.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Code

[View solution](../code/389_find_the_difference.py)
