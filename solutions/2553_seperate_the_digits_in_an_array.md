# 2553. Seperate the Digits in an Array

- **Difficulty:** Easy
- **Topic:** Array

https://leetcode.com/problems/separate-the-digits-in-an-array/description/

## Approach

Simple array manipulation. For each number, stringify it, split each character into a digit, convert back to `int`, and extend the result list. This avoids the need for repeated modulo/division operations.

## Complexity

- **Time:** O(D) where D is the total number of digits across all integers in `nums` — each digit is visited exactly once
- **Space:** O(D) for the output array

## Code

[View solution](../code/2553_seperate_the_digits_in_an_array.py)
