# 3970. Shortest Path With At Most K Consecutive Identical Characters

- **Difficulty:** Medium
- **Topic:** heap BFS

[LeetCode](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)

## Approach

If there is no requirement like at most k consecutive identical characters, this is a classic shortest path problem.
And there are so many ways to solve it, such as Dijkstra's algorithm, A* algorithms, or simpler ones like BFS, DFS, etc.

The only problem is that there is a constraint that the path must contain at most k consecutive identical characters.
So this problem is testing us if we are really familiar with all these path finding algorithms. The only thing we need
to modify from the algorithm is to keep track of the number of consecutive identical characters in the path.

Since this is a weighted graph, we can't just use a simple deque — we need Dijkstra's algorithm with a priority queue
(heap) to always process the lowest-cost state first.

The key extension over standard Dijkstra's is the state: instead of just `(node)`, we track
`(node, last_label, consecutive_count)`. When moving to a neighbor:
- If the neighbor's label matches `last_label`, increment `consecutive_count`.
- Otherwise, reset `consecutive_count` to 1.
- If `consecutive_count > k`, skip that neighbor entirely.

We deduplicate on the full state, so the same node can be visited multiple times as long as it arrives with a different consecutive count.

## Complexity

- **Time:** O((n·k + E) log(n·k)) — Dijkstra over the extended state space of n·k states, with E edges total
- **Space:** O(n·k + E) — visited dict of size n·k and adjacency list of size E

## Code

[View solution](../code/3970_shortest_path_with_at_most_k_consecutive_identical_characters.py)
