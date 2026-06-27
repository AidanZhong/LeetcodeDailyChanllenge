# 3971. Maximum Total Value

- **Difficulty:** Hard
- **Topic:** binary search

[LeetCode](https://leetcode.com/problems/maximum-total-value/)

## Approach

First instinct of this is using a priority queue(heap). Keep getting the maximum value from the heap and decay it and
add back to the heap. 100% correct. But it's too slow.

There is a trick way when we see the data constraint is 10^9. The only possible time complexity is O(logn). Which is the
binary search.

So, what about assuming we are getting the value no less than a certain value "W". Then we can use binary search to find
the optimal "W".

Now let's consider the data we are getting from, it is no longer a list of original values, it is a list of value with
all its positive decays.

```
[value[0], value[0] - decay[0], value[0] - decay[0] * 2, ...,
value[1], value[1] - decay[1], value[1] - decay[1] * 2, ...,
...
value[n], value[n] - decay[n], value[n] - decay[n] * 2, ...]
```

For index i, the number of decayed values still >= W is:
```
value[i] - decay[i] * (t - 1) >= W
t <= (value[i] - W) / decay[i] + 1
// since t is integer, so the maximum t should satisfy:
t = (value[i] - W) // decay[i] + 1
```
The sum of those t values is an arithmetic series: value[i] + (value[i] - decay[i]) + ... + (value[i] - decay[i]*(t-1)),
which simplifies to `t * value[i] - decay[i] * t * (t - 1) / 2`.

Do the same for each index i. Keep track of the sum value and count.
Then we got the total value and total count.

**Why binary search works:** as W increases, fewer decayed values qualify, so total count is monotonically decreasing in W.
This means we can binary search for the largest W such that `total_count >= m`.

**Edge case:** if even taking all values >= 1 fits within m selections, just return that sum directly.

**Assembling the final answer:** after finding the largest W where `count(W) >= m`, we take all values > W first (call
this `count_W+1` selections with sum `value_W+1`), then fill the remaining `m - count_W+1` slots each contributing exactly
W. This ensures we use all m selections optimally.

## Complexity

- **Time:** O(n log(max_value)) — binary search over [1, max(value)], each iteration scans all n indices
- **Space:** O(1)

## Code

[View solution](../code/3971_maximum_total_value.py)
