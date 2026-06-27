# 1189. Maximum number of balloons

- **Difficulty:** easy
- **Topic:** hash set

[LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/)

## Approach

count the number of each character in the string. A balloon is 1 'a', 1 'b', 2 'l', 2 'o' and 1 'n'.
Then count the total number of the text of each character. And use them to divide the amount of same character in the "
balloon". The answer is the minimum of all the divisions.

## Complexity

- **Time:**
- **Space:**

## Code

[View solution](../code/1189_maximum_number_of_balloons.py)
