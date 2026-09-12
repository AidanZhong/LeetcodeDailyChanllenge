# 3658. GCD of Odd and Even Sums

- **Difficulty:** Easy
- **Topic:** Math

[LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums/)

## Approach

Since

```
odd sum = (1 + 1 + (n-1)×2) × n / 2
        = n²

even sum = n² + n
         = n(n+1)
```

So, the GCD is $n$


## Complexity

- **Time:** O(1)
- **Space:** O(1)

## Code

[View solution](../code/3658_gcd_of_odd_and_even_sums.py)
