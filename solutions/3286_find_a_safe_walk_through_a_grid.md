# 3286. Find a Safe Walk Through a Grid

- **Difficulty:** Medium
- **Topic:** BFS

[LeetCode](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/)

## Approach

Use BFS with recording current health to try to find a path. In case some of the node could be visited first with lower
health. We are going to use heap(priority queue) to keep poping the highest health possible path.

## Complexity

- **Time:** O(mn)
- **Space:** O(mn)

## Code

[View solution](../code/3286_find_a_safe_walk_through_a_grid.py)
