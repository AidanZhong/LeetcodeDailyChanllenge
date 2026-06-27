# 3660. Jump Game IX

- **Difficulty:** Medium
- **Topic:** DSU

[LeetCode](https://leetcode.com/problems/jump-game-ix/)

## Approach

The jump rules are symmetric: from `i` you can jump forward to `j > i` if `nums[j] < nums[i]`, and from `j` you can jump backward to `i` if `nums[i] > nums[j]` — the same condition. So the graph is **undirected**, and the answer for each index is the maximum value in its connected component.

Use **[DSU (Disjoint Set Union)](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)** to group connected components, but avoid the naive O(n²) approach of checking every pair.

**Key insight — monotone stack with min-value tracking:**

Process indices **right to left**. Maintain a stack of `(dsu_representative, min_value_in_component)` where the top always holds the smallest `min_value`.

For each index `i` with value `v`:
1. Pop every stack entry whose `min_value < v`. That component contains some `j > i` with `nums[j] < v`, meaning a direct edge `(i, j)` exists — union `i` with that component.
2. Track the running minimum across all pops.
3. Push `(find(i), cur_min)` back onto the stack.

Once a component is merged, its minimum value is inherited by the new merged component, so future left-side elements can still trigger unions through it. Each index is pushed and popped at most once.

Finally, scan once to find each component's maximum value and build the answer array.

## Complexity

- **Time:** O(n · α(n)) ≈ O(n) — each index is pushed/popped once; each union is O(α(n))
- **Space:** O(n) — DSU arrays and stack

## Code

[View solution](../code/3660_jump_game_ix.py)
