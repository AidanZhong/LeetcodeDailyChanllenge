# 3756. Concatenate Non-Zero Digits and Multiply by Sum II

- **Difficulty:** Medium
- **Topic:** Prefix Sum, Math

[LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/)

## Approach

The problem seems to be easy since the brutal force is easy to approach. But it will exceed the time limit.

### 1 Identify the bottleneck
For each query, [l, r], we need 2 things:
1. the **sum** of the substring
2. the number $x$ formed by concatenating non-zero digits

Well the **sum** is easy since we could use prefix sum and it is O(1). The real challenge is how do we compute $x$ efficiently. Can we do it in O(1)? What make this hard is there are 0s in the string, otherwise we could simply use prefix for it.

### 2 Pretend there is no zeros
Since the bottleneck is the zeros in the string. What if we pretend the zeros don't exist? For example $s='10203004'$. We extract all the non-zero numbers called $n\_zero = [1,2,3,4]$.

Define $formed[i]$ is the number formed from [0..i] from $n\_zero$. Then

$$formed[i] = formed[i-1] * 10 + n\_zero[i]$$

So, for any range query from [a, b]. The formed number $x$ is

$$x = formed[b] - formed[a-1] * 10^{(b-a+1)}$$

Which is O(1)

### 3 Bridge the gap
Now let's come back to the original question. There are multiple zeros in the string and querying from [l, r]. How do we convert it into querying from [a, b] in $n\_zero$?

Observe the two arrays:

```
s = [1, 0, 2, 0, 3, 0, 0, 4]
n_zero = [1, 2, 3, 4]
```

Think about querying from [l, r]. In $n\_zero$, $a$ means how many non-zero digits are there in front of $l$ and $b$ means how many non-zero digits are there until $r$.

To achieve that, we could use a count array.

Define $non\_zero\_count[i]$ means how many non-zero elements are there in [0..i].

so

```
s =              [1, 0, 2, 0, 3, 0, 0, 4]
n_zero =         [1,    2,    3,       4]
non_zero_count = [1, 1, 2, 2, 3, 3, 3, 4]
```

For a query [l, r] converting into [a, b]

```
a = non_zero_count[l - 1]
b = non_zero_count[r] - 1
```

Put them all together, we could get each query in O(1) time complexity.

## Complexity

- **Time:** O(n) to build the prefix arrays, then O(1) per query, so O(n + q) overall for a string of length n and q queries.
- **Space:** O(n) for the prefix arrays ($pre\_sum$, $non\_zero\_count$, $formed$).

## Code

[View solution](../code/3756_concatenate_non-zero_digits_and_multiply_by_sum_ii.py)
