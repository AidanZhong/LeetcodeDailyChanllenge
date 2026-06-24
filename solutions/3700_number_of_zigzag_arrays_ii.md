# 3700. Number of ZigZag Arrays II

- **Difficulty:** Hard
- **Topic:** Dynamic programming

## Approach

This is actually the same as problem 3699. Only the input constraints are different. The n now is 10^9, which means the
previous solution is not feasible. O(n*(r - l)) is obviously not feasible.

But this time the l and r sits in a much smaller range, 1 <= l < r <= 75. Define m = r - l + 1

Same definition dp as in 3699. 
dp[i][v][s] as the number of valid zigzag arrays of length i + 1, ending with value v, and the last step is s(+, or -).

Let us observe the transition function:

$$dp[i][x][+] = \sum_{y=l}^{x-1} dp[i-1][y][-] \qquad dp[i][x][-] = \sum_{y=x+1}^{r} dp[i-1][y][+]$$

**Base case:** `dp[0][v][+] = dp[0][v][-] = 1` for every `v` in `[l, r]` — a length-1 array has no predecessor, so every value is valid, and both direction-placeholders start at 1.

**Final answer (length n):**

$$\text{answer} = \sum_{v=l}^{r} \big(dp[n-1][v][+] + dp[n-1][v][-]\big) \pmod{10^9+7}$$

It's easy to recognize that the transition is linear and time-invariant. 
Let's call dp[i][l+x][+] as "+x". The state vector has size of 2m.

Let us write the transition as a matrix format

$$V_i = M \cdot V_{i-1}$$

where `V_i` is the state vector of size `2m` ordered as `[+1, +2, ..., +m, -1, -2, ..., -m]`, and `M` is a fixed `(2m)×(2m)` matrix.

### Building M

`M` splits into four `m×m` blocks. The top-left (`+`→`+`) and bottom-right (`-`→`-`) blocks are all zero — directions never reinforce themselves directly. Only the off-diagonal blocks are nonzero:

$$M = \begin{pmatrix} 0 & L \\ U & 0 \end{pmatrix}$$

- `L[x][y] = 1` if `y < x`, else `0` — **strictly lower-triangular** matrix of 1s. Encodes `dp[i][x][+] = sum of dp[i-1][y][-]` for `y < x`.
- `U[x][y] = 1` if `y > x`, else `0` — **strictly upper-triangular** matrix of 1s. Encodes `dp[i][x][-] = sum of dp[i-1][y][+]` for `y > x`.

Note `U = Lᵗ` (transpose) — a consequence of the symmetric "less than / greater than" structure of the two transition rules. This means you only need to construct `L` and can derive `U` for free.

**Example, m=4:**

$$L = \begin{pmatrix} 0&0&0&0\\ 1&0&0&0\\ 1&1&0&0\\ 1&1&1&0 \end{pmatrix} \qquad U = \begin{pmatrix} 0&1&1&1\\ 0&0&1&1\\ 0&0&0&1\\ 0&0&0&0 \end{pmatrix}$$

**Example, m=5:**

$$L = \begin{pmatrix} 0&0&0&0&0\\ 1&0&0&0&0\\ 1&1&0&0&0\\ 1&1&1&0&0\\ 1&1&1&1&0 \end{pmatrix} \qquad U = \begin{pmatrix} 0&1&1&1&1\\ 0&0&1&1&1\\ 0&0&0&1&1\\ 0&0&0&0&1\\ 0&0&0&0&0 \end{pmatrix}$$

Readers can try to verify these matrix multiply by themselves.

It is obvious that the matrix is a constant instead of a variable changes overtime. So

$$V_{n-1} = M^{\,n-1} \cdot V_0$$

And the final answer will be the sum of all values in $V_{n-1}$

## Complexity

- **Time:**
- **Space:**

## Code

[View solution](../code/3700_number_of_zigzag_arrays_ii.py)