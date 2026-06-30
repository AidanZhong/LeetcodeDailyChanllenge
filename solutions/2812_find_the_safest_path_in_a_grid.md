# 2812. Find the Safest Path in a Grid

- **Difficulty:** Medium
- **Topic:** BFS, binary search

[LeetCode](https://leetcode.com/problems/find-the-safest-path-in-a-grid/)

## Approach

Firstly, we can get a matrix marking the safeness of each cell by multi-source BFS. (Starting with all the thieves with safeness 0, and expanding outward layer by layer)

Then, we need to find a path with the largest safeness. Suppose the path contains no cell with safeness smaller than `limit`. We could use BFS or DFS to verify if such a path exists (only visiting cells with safeness ≥ `limit`). Since the feasibility is monotonic — if a path exists for `limit = k`, it also exists for any `limit < k` — we can binary search to find the biggest valid `limit`.

## Complexity

- **Time:** O(n² log n) — O(n²) for the multi-source BFS, plus O(log n) binary search iterations each running an O(n²) path check.
- **Space:** O(n²)

## Code

[View solution](../code/2812_find_the_safest_path_in_a_grid.py)