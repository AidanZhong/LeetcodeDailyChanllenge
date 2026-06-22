# Problem: Shortest Path With At Most K Consecutive Identical Characters
# Topic: heap BFS
# Difficulty: Medium

'''
You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.

You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.

Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.



Example 1:

Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1

Output: 3

Explanation:

The optimal valid path from node 0 to node 2 is as follows:

Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.
The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.
'''
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj_dict = defaultdict(list)
        for u, v, w in edges:
            adj_dict[u].append((v, w))

        # start with 0
        q = [(0, 0, labels[0], 1)]
        visited = {}
        while q:
            total_weight, node, last_label, consecutive_count = heapq.heappop(q)
            if node == n - 1:
                return total_weight
            state = (node, last_label, consecutive_count)
            if state in visited:
                continue
            visited[state] = total_weight
            # find adjacent nodes
            for adj, weight in adj_dict[node]:
                if last_label == labels[adj]:
                    new_consecutive_count = consecutive_count + 1
                else:
                    new_consecutive_count = 1
                if new_consecutive_count > k:
                    continue
                if (adj, labels[adj], new_consecutive_count) in visited:
                    continue
                heapq.heappush(q, (total_weight + weight, adj, labels[adj], new_consecutive_count))
        return -1
