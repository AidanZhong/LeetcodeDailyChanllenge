# 1301. Number of Paths with Max Score

- **Difficulty:** Hard
- **Topic:** Dynamic programming

[LeetCode](https://leetcode.com/problems/number-of-paths-with-max-score/)

## Approach

Since we can only move towards up, left or up-left. So we cannot go back to each cell. Which means we could use dynamic programming to record any status of a cell.

Define $dp(i, j)$ is the largest score of the path and the number of cell on $i$ th row, $j$ th col. It will return a tuple with max score call it $s(i, j)$ and the number of path call it $n(i, j)$. $dp(i, j)$ is determined by the cell next to it which is reachable. i.e. $dp(i+1, j), dp(i, j+1), dp(i+1, j+1)$. We call it set $dp\_next$. And we call the one with largest score $dp(x, y)$.

If one of them got larger score than other two, It means we could only go that way to get maximum score.

$$s(i, j) = s(x, y) + score(i, j)$$
$$n(i, j) = n(x, y) $$

If two of them are the same and larger than other one. It means we could go both way to get maximum score.

$$s(i, j) = s(x_1, y_1) + score(i, j)$$
$$n(i, j) = n(x_1, y_1) + n(x_2, y_2)$$

If three of them are the same. It means we could go either of them.

$$s(i, j) = s(x_1, y_1) + score(i, j)$$
$$n(i, j) = n(x_1, y_1) + n(x_2, y_2) + n(x_3, y_3)$$

Now let us consider the borders.

$$ dp(0, 0) = 0, 1 $$
$$ dp(i, j) = 0, 0 (board[i][j] == 'X') $$


## Complexity

- **Time:** $O(n^2)$, each of the $n^2$ cells is computed once, doing $O(1)$ work (sorting 3 fixed-size tuples).
- **Space:** $O(n^2)$ for the memoization cache, plus $O(n)$ recursion stack depth.

## Code

[View solution](../code/1301_number_of_paths_with_max_score.py)
