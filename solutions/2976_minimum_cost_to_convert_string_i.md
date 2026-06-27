# 2976. Minimum Cost to Convert String I

- **Difficulty:** Medium
- **Topic:** Graph, Shortest Path

[LeetCode](https://leetcode.com/problems/minimum-cost-to-convert-string-i/)

## Approach

Treat each letter as a node of a graph. This problem is converted into finding multiple shortest paths in a directed
weighted graph.

We could use BFS, DFS, Dijkstra, A*, etc. Note that BFS only works for unweighted graphs. Since edges here have
different costs, we need Dijkstra's algorithm (min-heap on accumulated distance) instead.

For each position i in source, run Dijkstra from `source[i]` to `target[i]`:

1. Init the heap with the starting node at distance 0.
2. Each time pop from the heap, we are getting the closest unvisited node reachable so far.
3. If the node is the target, return the distance.
4. If it is not, push all its adjacent nodes (except visited ones to avoid infinite loops) onto the heap.
5. If the heap is empty and we still didn't reach the target node, there is no valid path — return -1.

Since there are only 26 lowercase letters, each Dijkstra runs on a graph of at most 26 nodes regardless of the
input size.

## Complexity

- **Time:** O(m × k log k) — m Dijkstra calls (one per character position), each over a graph with at most k edges
- **Space:** O(k) — adjacency list storage

## Code

[View solution](../code/2976_minimum_cost_to_convert_string_i.py)
