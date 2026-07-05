# 1288. Remove Covered Intervals

- **Difficulty:** Medium
- **Topic:** Sorting, Array

[LeetCode](https://leetcode.com/problems/remove-covered-intervals/)

## Approach

Firstly sort the array, with asc on left boarder, and desc on right boarder. So that each time we get an interval, it is the smallest left boarder we can find, we record the right boarder of it $cur\_r$. And go to the next interval. If the next interval has a right boarder no bigger than $cur\_r$. It is covered by previous one. It will count as a covered one. Once the right boarder is bigger than $cur\_r$, update $cur\_r$.

Finally use the length of whole intervals list and substract the counted covered one.

## Complexity

- **Time:** $O(n \log n)$ — dominated by sorting; the single pass afterward is $O(n)$.
- **Space:** $O(n)$ worst case for Timsort's auxiliary space (or $O(\log n)$ typical); $O(1)$ extra beyond the sort itself.

## Code

[View solution](../code/1288_remove_covered_intervals.py)