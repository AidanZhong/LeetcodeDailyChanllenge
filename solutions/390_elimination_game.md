# 390. Elimination Game

- **Difficulty:** Medium
- **Topic:** Math

[LeetCode](https://leetcode.com/problems/elimination-game/)

## Approach

If we simply simulate the game, the large $n$ will make the solution time out.

Observe the array we will find that after any operation, it will always be an arithmetic array. So for an arithmetic array, what we need to represent it is $head, gap, totalElements$. Also for the operation, we need a variable to record the $direction$ of the operation.

Each operation:

1. The $head$ will be eliminated, the new head will be $head + gap$, unless going from right to left with an even $totalElements$, in which case it remains the same.
2. The $gap$ will be doubled.
3. The $totalElements$ will be shrinked to half.
4. The $direction$ will change.

Do the operation until the $totalElements$ is 1, which is our answer.

## Complexity

- **Time:** O(log n)
- **Space:** O(1)

## Code

[View solution](../code/390_elimination_game.py)