# Problem: Elimination Game
# Topic: Math
# Difficulty: Medium


class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        gap = 1
        remaining_count = n
        direction = 0  # 0 means left to right, 1 means right to left
        while remaining_count > 1:
            # do the elimination
            if direction == 0:
                head += gap
            elif remaining_count % 2 == 1:
                # head will only change if its odd number
                head += gap

            direction = 1 - direction  # change direction
            gap *= 2
            remaining_count //= 2
        return head


print(Solution().lastRemaining(n=9))
print(Solution().lastRemaining(n=1))
print(Solution().lastRemaining(n=2))
