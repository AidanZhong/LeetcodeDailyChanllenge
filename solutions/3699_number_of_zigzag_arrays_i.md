# 3699. Number of ZigZag Arrays I

- **Difficulty:** Hard
- **Topic:** Dynamic programming

[LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-i/)

## Approach

Firstly, we need to understand the "ZigZag". No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.

Now assume we have a sequence of a[i] a[i+1] a[i+2], set c[i] = {+, if a[i] < a[i+1], -, if a[i] > a[i+1]}.
For example, [4, 5, 4] with c = [+, -], [5, 4, 5] with c = [-, +]. We call this sequence of c, sign sequence.

Now the rule 2 becomes: for each i, c[i] != c[i+1]

And of course, counting the sign patterns is easy. It's either starts with + or -, then alternating for each index.
So how to count the number of actual arrays from sign sequence? We need DP(dynamic programming) to keep track of at each
index, what value do we have.

Question for you: If I want to build the array from left to right, value by value, what information do I need to know
about
the array so far in order to decide which values are legal for the next element?

The answer is simple, we need to know the current position(index), current value, and the direction(sign) of last step.
That is how we define a state.
Define:
dp[i][v][s] as the number of valid zigzag arrays of length i + 1, ending with value v, and the last step is s(+, or -).

Now let us consider the state change. For example, dp[5][7][+] = 123, to extend to position 6 from this state,
we can pick any x < 7, contributing dp[5][7][+] to dp[6][x][-]. More generally, dp[6][x][-] sums all dp[5][y][+]
for y > x — every previous value greater than x can step down to x.

Now generalize the state change to all possible states.

```
dp[i][x][-] = sum(dp[i-1][y][+]) (x < y <= r)
dp[i][x][+] = sum(dp[i-1][y][-]) (l <= y < x)
```

The last trick of the problem: calculating the sum by brute force is still going to exceed the time limit.
The solution is to use prefix sum arrays. We maintain two rolling arrays — one for the + direction and one for the -
direction — where `pre_plus[k]` = sum of dp[i-1][x][+] for x in [l, l+k-1], and similarly for `pre_minus`. This
allows each range sum to be computed in O(1) as a difference of two prefix values. We only need the previous step's
two arrays (not all n layers), since once step i is computed, the step i-1 arrays are no longer needed.

Before coding, we need to figure out the boundary of the dp states. dp[0][v][s] = 1 for all v in [l, r] and both
directions s — the first element has no predecessor, so any value is valid and there is exactly 1 array of length 1
ending at v. The direction s at i=0 is just a placeholder indicating which direction the next step must go.

Finally, the answer is the sum of all dp[n-1][v][+] and dp[n-1][v][-] for v in [l, r], i.e., the total count of
valid zigzag arrays regardless of which direction the last step was.

## Complexity

- **Time:** O(n × (r - l)), two prefix sum arrays of size r-l+2 are rebuilt each of the n steps
- **Space:** O(r - l), only the two rolling prefix sum arrays are kept at any time

## Code

[View solution](../code/3699_number_of_zigzag_arrays_i.py)
