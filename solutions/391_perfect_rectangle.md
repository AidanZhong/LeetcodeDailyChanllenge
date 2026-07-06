# 391. Perfect Rectangle

- **Difficulty:** Hard
- **Topic:** Geometry

[LeetCode](https://leetcode.com/problems/perfect-rectangle/)

## Approach

Assume we can form a perfect rectangle. So the corner of the big rectangle should be the smallest $x_i$, smallest $y_i$ as the bottom left corner, biggest $a_i$, biggest $b_i$ as the top right corner. All we have to do is check if all the rectangles could fill the big one without overlaping each other.

1. Area check. Check the sum of area of all the rectangles, and compare to the big one, it should be the same otherwise return $false$.
2. Corner count check. Except the corner that form the big rectangle, all the other corners should be overlapping at even amount of times. (Odd amount of time will form a new corner to the whole graph). This ensures no new corners being formed.

Combined with both checking, we could ensure that the rectangles could form the big one without overlapping.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Code

[View solution](../code/391_perfect_rectangle.py)
