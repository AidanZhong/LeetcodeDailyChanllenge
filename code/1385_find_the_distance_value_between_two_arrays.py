# Problem: Find the Distance Value Between Two Arrays
# Topic: Array
# Difficulty: Easy


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    break
            else:
                count += 1
        return count
