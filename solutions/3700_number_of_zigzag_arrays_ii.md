# 3700. Number of ZigZag Arrays II

- **Difficulty:** Hard
- **Topic:** Dynamic programming

## Approach

This is actually the same as problem 3699. Only the input constraints are different. The n now is 10^9, which means the
previous solution is not feasible. O(n*(r - l)) is obviously not feasible.

But this time the l and r sits in a much smaller range, 1 <= l < r <= 75. 

Same definition dp as in 3699. 
dp[i][v][s] as the number of valid zigzag arrays of length i + 1, ending with value v, and the last step is s(+, or -).

Let us observe the transition function:

$$dp[i][x][+] = \sum_{y=l}^{x-1} dp[i-1][y][-] \qquad dp[i][x][-] = \sum_{y=x+1}^{r} dp[i-1][y][+]$$

**Base case:** `dp[0][v][+] = dp[0][v][-] = 1` for every `v` in `[l, r]` — a length-1 array has no predecessor, so every value is valid, and both direction-placeholders start at 1.

**Final answer (length n):**

$$\text{answer} = \sum_{v=l}^{r} \big(dp[n-1][v][+] + dp[n-1][v][-]\big) \pmod{10^9+7}$$

It's 

## Complexity

- **Time:**
- **Space:**

## Code

[View solution](../code/3700_number_of_zigzag_arrays_ii.py)

# Number of ZigZag Arrays I & II — Full Thought Process

## Step 1: Reformulate the rules as an alternating-sign condition

A ZigZag array of length `n` with values in `[l, r]` must satisfy:

1. No two adjacent elements are equal.
2. No three consecutive elements are strictly increasing or strictly decreasing.

Define the step-direction sequence:

$$c_i = \begin{cases} + & \text{if } a[i+1] > a[i] \\ - & \text{if } a[i+1] < a[i] \end{cases}$$

For any triple `a[i], a[i+1], a[i+2]`, its shape is fully determined by `(c_i, c_{i+1})`:

- `++` → strictly increasing (forbidden)
- `--` → strictly decreasing (forbidden)
- `+-` or `-+` → zigzag (allowed)

So rule 2 becomes simply: **no two consecutive signs in the sequence `c_0, c_1, ..., c_{n-2}` are equal** — i.e., the sign sequence must strictly alternate (`+-+-...` or `-+-+...`).

This collapses two awkward rules into one clean structural rule.

## Step 2: Why we still need a DP (not just counting sign patterns)

For small examples, counting alternating sign sequences alone can coincidentally match the answer (e.g. `n=3, l=4, r=5`), but in general **one sign sequence corresponds to many different arrays**, since at each step we also choose an actual value, and how many choices are legal depends on how much room is left in `[l, r]`.

So we need to track, at each position, **what value we are at** — not just the abstract direction.

## Step 3: Define the DP state

`dp[i][v][s]` = number of valid arrays of length `i+1`, ending with value `v`, where the last step taken was direction `s ∈ {+, -}`.

This state is **sufficient** (Markov property): to decide what values are legal next, we only need the current value and the direction of the last step — nothing further back matters.

## Step 4: The transition

To end at value `x` via an increase, the previous value `y` must be `< x`, and the step *into* `y` must have been a decrease (so that decrease-then-increase keeps alternating). Symmetrically for decreases:

$$dp[i][x][+] = \sum_{y=l}^{x-1} dp[i-1][y][-] \qquad dp[i][x][-] = \sum_{y=x+1}^{r} dp[i-1][y][+]$$

**Base case:** `dp[0][v][+] = dp[0][v][-] = 1` for every `v` in `[l, r]` — a length-1 array has no predecessor, so every value is valid, and both direction-placeholders start at 1.

**Final answer (length n):**

$$\text{answer} = \sum_{v=l}^{r} \big(dp[n-1][v][+] + dp[n-1][v][-]\big) \pmod{10^9+7}$$

## Step 5: Verify against Example 1

`n=3, l=4, r=5` → reindex values to `{1,2}`.

- `dp[0] = [+1,+2,-1,-2] = [1,1,1,1]`
- `dp[1][1][+] = 0` (nothing < 1); `dp[1][2][+] = dp[0][1][-] = 1`
  `dp[1][1][-] = dp[0][2][+] = 1`; `dp[1][2][-] = 0` (nothing > 2)
- `dp[2][1][+] = 0`; `dp[2][2][+] = dp[1][1][-] = 1`
  `dp[2][1][-] = dp[1][2][+] = 1`; `dp[2][2][-] = 0`
- Total = `0+1+1+0 = 2` ✓ matches the expected output.

The two sequences `[4,5,4]` and `[5,4,5]` correspond exactly to `dp[2][1][-]` and `dp[2][2][+]`.

## Step 6: 3699 — small n·m, prefix-sum DP

**Constraints:** `3 ≤ n ≤ 2000`, `1 ≤ l < r ≤ 2000`.

With `m = r - l + 1 ≤ 2000` and `n ≤ 2000`, a direct `O(n·m)` DP works, using prefix sums to compute each range-sum transition in O(1):

```python
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        up = [1] * (m + 1)    # 1-indexed; up[0] unused
        down = [1] * (m + 1)

        for i in range(2, n + 1):
            prefixDown = [0] * (m + 1)
            for v in range(1, m + 1):
                prefixDown[v] = (prefixDown[v-1] + down[v]) % MOD

            suffixUp = [0] * (m + 2)
            for v in range(m, 0, -1):
                suffixUp[v] = (suffixUp[v+1] + up[v]) % MOD

            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)
            for v in range(1, m + 1):
                new_up[v] = prefixDown[v-1]
                new_down[v] = suffixUp[v+1]

            up, down = new_up, new_down

        return sum(up[1:] + down[1:]) % MOD
```

**Complexity:** `O(n·m)` time, `O(m)` space. Fits comfortably since `n·m ≤ 4×10^6`.

## Step 7: 3700 — huge n, small m, matrix exponentiation

**Constraints:** `3 ≤ n ≤ 10^9`, `1 ≤ l < r ≤ 75`.

Now `n` is too large to loop over directly, but `m = r - l + 1 ≤ 75` is tiny. The key realization:

**The transition is linear and time-invariant** — same coefficients at every step, because they depend only on `l, r`, never on `i`. That means we can write the whole DP step as matrix-vector multiplication:

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

### Solving with repeated squaring

Since `V_0` represents length-1 arrays (all entries = 1) and each application of `M` advances the represented length by 1, reaching length `n` requires:

$$V_{n-1} = M^{\,n-1} \cdot V_0$$

Compute `M^{n-1}` via fast matrix exponentiation (repeated squaring): `O(log n)` matrix multiplications, each `O((2m)^3)`.

**Cost check:** `2m ≤ 150` → one multiply ≈ `150³ ≈ 3.4×10⁶` ops. `log₂(10^9) ≈ 30` multiplications → total ≈ `10^8` ops. Comfortably within typical time limits.

### Final answer

$$\text{answer} = \sum (\text{all entries of } V_{n-1}) \pmod{10^9+7}$$

## Step 8: The general lesson

Same DP state definition throughout (`dp[i][v][s]`) — only the **engine** for advancing through the `n` layers changes, based on which dimension is the bottleneck:

- **`m` is the bottleneck, `n` is small** → loop over layers, use prefix sums to make each layer `O(m)` instead of `O(m²)`. Total `O(n·m)`.
- **`n` is the bottleneck, `m` is small** → recognize the per-layer transition is linear and identical every step, collapse `n` repeated applications into a single matrix power `M^{n-1}`, computed in `O(log n)` matrix multiplications.

Whenever a DP's transition between layers is linear and doesn't depend on the layer index, and the number of layers is huge while the state size is small, **matrix exponentiation turns an O(n) problem into an O(log n) one**.