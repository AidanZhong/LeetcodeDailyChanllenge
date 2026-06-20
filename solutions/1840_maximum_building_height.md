# 1840. Maximum Building Height

- **Difficulty:** Hard
- **Topic:** Math

## Approach

Treat building 1 (height 0) and building n (max height n-1) as restrictions as well, so every segment between buildings is bounded on both sides.

For each pair of adjacent restrictions (i1, c1) and (i2, c2), define f(i1, c1, i2, c2) as the maximum height of any building between them:

- If the distance ≤ the height difference, one side dominates: peak = `min(c1, c2) + (i2 - i1)`.
- Otherwise the path forms a mountain (up then down): the peak sits at the midpoint where both slopes meet, giving peak = `(c1 + c2 + i2 - i1) // 2`.

The problem is that each restriction is only a one-sided bound until we account for both neighbors. We do two passes:

- **Left to right**: cap each restriction by what is reachable from the left — `c = min(c, c_prev + (i - i_prev))`. Compute f for each adjacent pair and store in `highest_buildings`.
- **Right to left**: cap each restriction by what is reachable from the right, then take the minimum with the already-stored value in `highest_buildings`.

After both passes each entry in `highest_buildings` is the true peak for that segment. Return the maximum.

## Complexity

- **Time:** O(R log R) — sorting the restrictions; both passes are O(R)
- **Space:** O(R) — for the modified restrictions list and `highest_buildings`

## Code

[View solution](../code/1840_maximum_building_height.py)
