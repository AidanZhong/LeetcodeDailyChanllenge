# Problem: Create Grid With Exactly One Path
# Topic: Simulation
# Difficulty: Easy


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # just go right m-1 times and down n-1 times
        ans = ['.' * n]
        for _ in range(1, m):
            ans.append('#' * (n - 1) + '.')
        return ans
