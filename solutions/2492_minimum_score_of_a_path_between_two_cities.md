# 2492. Minimum Score of a Path Between Two Cities

- **Difficulty:** Medium
- **Topic:** DSU

[LeetCode](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)

## Approach

This could be misunderstood as a path finding problem. 

But in case the problem stated the node could be visited multiple times and we are going to find the minimum $score$ which is minimum distance of a road. This is a **connection problem** instead of a path finding problem.

In other word, as long as the city 1 and n are connected, there will be a path. We call the connected graph $G$. And the problem is to find the shortest road in the connected graph $G$. (Because it is connected, there is always a way to visit the road that go from city 1 to city n).

For connection checking problems, there is a common technique called DSU (Disjoint Set Union, a.k.a. Union-Find, see [cp-algorithms](https://cp-algorithms.com/data_structures/disjoint_set_union.html)). We need to check the connection between nodes, and also update the shortest road it could go to.

## Complexity

- **Time:** $O((n + m) \alpha(n))$, where $m$ is the number of roads. With union by size and path compression, each `find`/`union` call runs in amortized inverse-Ackermann time, and `beautify` performs one more `find` per node.
- **Space:** $O(n)$ for the DSU parent, size, and score arrays.

## Code

[View solution](../code/2492_minimum_score_of_a_path_between_two_cities.py)
