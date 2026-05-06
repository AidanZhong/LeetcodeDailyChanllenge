# 1861. Rotating the Box

- **Difficulty:** Medium
- **Topic:** Matrix

## Approach

Since the box is rotated 90° clockwise, gravity effectively pulls stones to the right in the original grid. We can simulate this before performing the rotation.

For each row, append a sentinel obstacle `*` at the end. This avoids a special case for stones that would fall off the right edge — they simply stack against this sentinel just like any other obstacle.

Then scan each row left to right, counting stones `#`. When an obstacle `*` is encountered, place the counted stones immediately to its left (filling positions `idx - count` to `idx - 1`), and reset the counter. This correctly simulates gravity within each row.

Finally, rotate the entire grid 90° clockwise by reading columns top-to-bottom as rows. Since we appended a sentinel column, slice it off from the result with `[:-1]`.

## Complexity

- **Time:** O(m × n) — each cell is visited a constant number of times across the gravity simulation and the rotation.
- **Space:** O(m × n) — for the output grid.

## Code

[View solution](../code/1861_rotating_the_box.py)
