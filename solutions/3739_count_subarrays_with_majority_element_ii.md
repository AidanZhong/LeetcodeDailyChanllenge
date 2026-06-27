# 3739. Count Subarrays With Majority Element II

- **Difficulty:** Hard
- **Topic:** prefix sum

[LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-ii/)

## Approach

Since we only care about the values in the array where it is equals to "target".
So we can update the array to 1 and -1, 1

```python3
nums = [1 if i == target else -1 for i in nums]
```

We need target strictly more than half of the array, means for any subarray [l, r].
pre_sum[r+1] - pre_sum[l] > 0. Which means, for each index, we need to know how many of the previous element in
prefix sum is smaller than current one.

now for each right endpoint "r", define

```
valid = how many endpoints l <= r have prefix[l] < prefix[r+1]
```

each step, ans += valid

Now the question is: how do we update `valid` efficiently?
We can use a dictionary "pre_dict" (Hash map) to record until index i, how many times does each element appears.
For example:

```
pre_sum = [-1, 0, 1, ... ]
# when i == 2, pre_sum[i] = 1
pre_dict = {-1: 1, 0: 1}
# we need to add all pre_dict[k] (k<pre_sum[i])
```

But searching all the k is still too slow. Notice that the pre_sum only change +-1 at a time.
So we can use another variable "threshold" to record the sum of all pre_dict[k], and each time it +1, "threshold" +=
pre_dict[cur] otherwise minus pre_dict[cur - 1].

Here `cur` is the prefix value BEFORE the step. When going up, the window expands to include values equal to `cur` (the
old boundary). When going down, the window shrinks to exclude values equal to `cur - 1` (the new boundary).

Say `cur = 0` and `pre_dict = {-1:3, 0:2, 1:1}`, so `threshold = pre_dict[-1] = 3` (only values strictly below 0).

- **Element = +1, cur goes 0 → 1:** threshold should now count values strictly below 1, meaning we gain all entries with value 0. So `threshold += pre_dict[0] = 2` → `threshold = 5`.
- **Element = -1, cur goes 0 → -1:** threshold should now count values strictly below -1, meaning we lose all entries with value -1. So `threshold -= pre_dict[-1] = 3` → `threshold = 0`.

For example, `nums = [1,2,2,3]`, `target = 2` → transformed `[-1, +1, +1, -1]`:

```
init: pre_dict = {0:1}, threshold = 0, cur = 0, ans = 0

step 1: element = -1, cur = 0 → -1
  threshold -= pre_dict[cur-1] = pre_dict[-1] = 0  →  threshold = 0
  ans += 0  →  ans = 0
  register cur=-1: pre_dict = {0:1, -1:1}

step 2: element = +1, cur = -1 → 0
  threshold += pre_dict[cur] = pre_dict[-1] = 1     →  threshold = 1
  ans += 1  →  ans = 1
  register cur=0: pre_dict = {0:2, -1:1}

step 3: element = +1, cur = 0 → 1
  threshold += pre_dict[cur] = pre_dict[0] = 2      →  threshold = 3
  ans += 3  →  ans = 4
  register cur=1: pre_dict = {0:2, -1:1, 1:1}

step 4: element = -1, cur = 1 → 0
  threshold -= pre_dict[cur-1] = pre_dict[0] = 2    →  threshold = 1
  ans += 1  →  ans = 5
```

## Complexity

- **Time:** O(n) — single pass, O(1) update per step
- **Space:** O(n) — pre_dict holds at most one entry per distinct prefix value

## Code

[View solution](../code/3739_count_subarrays_with_majority_element_ii.py)
