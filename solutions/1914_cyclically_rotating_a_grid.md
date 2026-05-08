# 1914. Cyclically Rotating a Grid

- **Difficulty:** Medium
- **Topic:** Matrix

https://leetcode.com/problems/cyclically-rotating-a-grid/description/

## Approach

To simplify the problem, we can convert each layer into an array. The apply the rotation to each array. Finally refill
the grid.

## Complexity

- **Time:** O(m × n)
  - Extracting all layers: O(m × n) — each cell is visited exactly once across all layers
  - Rotating each layer array: O(perimeter) per layer via slicing → O(m × n) total
  - Refilling the grid: O(m × n) — each cell is written exactly once
- **Space:** O(m × n)
  - `layer_arrays` stores all elements across all layers: O(m × n)
  - Output grid `ans`: O(m × n)

## Code

[View solution](../code/1914_cyclically_rotating_a_grid.py)
