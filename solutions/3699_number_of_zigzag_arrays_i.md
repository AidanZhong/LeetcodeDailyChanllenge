# 3699. Number of ZigZag Arrays I

- **Difficulty:** Hard
- **Topic:** Dynamic programming

## Approach

Firstly, we need to understand the "ZigZag". No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.

Now assume we have a sequence of a[i] a[i+1] a[i+2], set c[i] = {+, if a[i] < a[i+1], -, if a[i] > a[i+1]}.
For example, [4, 5, 4] with c = [+, -], [5, 4, 5] with c = [-, +]. We call this sequence of c, sign sequence.

Now the rule 2 becomes: for each i, c[i] != c[i+1]

And of course, counting the sign patterns is easy. Its either starts with + or -, then alternating for each index.
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
dp[6][x][-] = dp[5][7][+] + ... (other states) (l <= x < 7) which means it is a one-to-one extension from one state.

Now generalize the state change to all possible states.

```
dp[i][x][-] = sum(dp[i-1][y][+]) (x < y <= r)
dp[i][x][+] = sum(dp[i-1][y][-]) (l <= y < x)
```

The last trick of the problem, is to calculate the sum is by brutal force is still gonna exceed the time limit.
The solution is simply to use a prefix sum array. (We only need 1 pre_sum array for each index i tho, we don't need n 
pre_sum arrays, we just need 1, since after index i is being calculated, the pre_sum array is no longer needed)

Before coding, we need to figure out the boundary of the dp states. dp[0][x][s] = 1 (since the first element is always
legal and only one possible array)

Finally, we need to return the sum of each final possible state.

## Complexity

- **Time:**
- **Space:**

## Code

[View solution](../code/3699_number_of_zigzag_arrays_i.py)
