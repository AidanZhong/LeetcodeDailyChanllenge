# 3968. Maximum Manhattan Distance After All Moves

- **Difficulty:** Medium
- **Topic:** simulation

[LeetCode](https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/)

## Approach

No matter how you moved, the "_" move can only increase the Manhattan distance by 1 and can always be done.

So what we do is to simulate the moves and count the _ move. Calculate the Manhattan distance after all moves and plus
the number of "_" move.

## Complexity

- **Time:** O(n) — single pass through the moves string
- **Space:** O(1) — only a few variables regardless of input size

## Code

[View solution](../code/3968_maximum_manhattan_distance_after_all_moves.py)
