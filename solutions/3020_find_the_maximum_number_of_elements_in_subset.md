# 3020. Find the Maximum Number of Elements in Subset

- **Difficulty:** Medium
- **Topic:** Hash set

[LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/)

## Approach

Record the number of appearance of each element into a dictionary(Hash set).

Element 1 is an exception. Assume there are $x$ 1s in the list. If $x$ is odd, it could use all the 1s to form a list.
Otherwise use $x-1$ 1s to form a list

For other elements, try to use each of them as the start to form the array. Remember to use a visited set to avoid
duplicated computing. E.g., we already tried start with $2$, then we are not trying to start with $4$.

## Complexity

- **Time:** O(n log n) — O(n) to build the frequency dict, O(u log u) to sort unique keys (u ≤ n), and O(u) total across all chain traversals since each element is visited at most once
- **Space:** O(n) — frequency dict and visited set

## Code

[View solution](../code/3020_find_the_maximum_number_of_elements_in_subset.py)
