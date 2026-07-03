# 3620. Network Recovery Pathways

- **Difficulty:** Hard
- **Topic:** Shortest path

[LeetCode](https://leetcode.com/problems/network-recovery-pathways/)

## Approach

Let us summary all the constraints in the problem:

1. The total cost should not exceed $k$
2. All nodes on the path should be online, which means we could eliminate all the edges with node offline on either
   side.

The $score$ of the path is defined as the minimum edge cost of the path. And we are going to find the maximum path score.

The simple thought could be calculate all the valid paths and find the maximum $score$. But the thing is there are too many possibilities.

What if we add more constraints by our own?

We could treat path $score$ as a new constraint. 

1. We set a constraint that path $score$ should be no less than $s$. 
2. Then we could try to find the valid path. 
3. If it exists, it means for all $v<s$, there are valid path have $score$ no less than $v$. 
4. We should make the $s$ higher to search for the maximum. 
5. If it does not exist, it means $s$ is too big and we need a smaller one.
6. In this case, we could use binary search to get the maximum $s$. Which is the answer to the problem.
7. While doing the binary search of $s$, the minimum is $0$ and the maximum is $k$.

Let us rephrase the new constraint. 

A path $score$ which is no less than $s$ means, the minimum edge cost of the path should be larger than $s$. Which means edge should have a cost more than $s$ during the path finding. 

The remaining will be a path finding problem.

## Complexity

- **Time:** $O((n + m) \log n \log k)$ — binary search over $s \in [0, k]$ takes $O(\log k)$ iterations, and each iteration runs Dijkstra (with lazy deletion) in $O((n + m) \log n)$.
- **Space:** $O(n + m)$ for the adjacency list, visited set, and heap.

## Code

[View solution](../code/3620_network_recovery_pathways.py)
