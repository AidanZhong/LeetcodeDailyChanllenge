# Problem: Minimum Jumps to Reach End via Prime Teleportation
# Topic: BFS, SPF
# Difficulty: Medium

"""
You are given an integer array nums of length n.

You start at index 0, and your goal is to reach index n - 1.

From any index i, you may perform one of the following operations:

Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
Return the minimum number of jumps required to reach index n - 1.

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 106
"""

from collections import deque, defaultdict
from typing import List


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        # pre compute the SPF
        MAX_NUM = max(nums) + 1
        spf = list(range(MAX_NUM))
        for i in range(2, int(MAX_NUM ** 0.5) + 1):
            if spf[i] != i: # isn't prime number
                continue
            for j in range(i * i, MAX_NUM, i): # try to find the multiple of i
                if spf[j] == j:
                    spf[j] = i # update the SPF


        teleportation = defaultdict(set)
        for i, num in enumerate(nums):
            x = num
            while x > 1:
                prime = spf[x]
                teleportation[prime].add(i)
                # consume all copies of this prime before moving to the next
                # e.g. num=12 (2x2x3): prime=2, x: 12->6->3, then outer loop finds prime=3
                # without this, x=12->6 would re-enter outer loop with prime=2 again (duplicate)
                while x % prime == 0:
                    x //= prime

        q = deque()
        q.append((0, nums[0], 0))
        visited = set()
        visited.add(0)
        while q:
            idx, number, jumps = q.popleft()
            if idx == len(nums) - 1:
                return jumps
            # adjacent is accessible
            if idx + 1 < len(nums) and (idx + 1 not in visited):
                q.append((idx + 1, nums[idx + 1], jumps + 1))
                visited.add(idx + 1)
            if idx - 1 >= 0 and (idx - 1 not in visited):
                q.append((idx - 1, nums[idx - 1], jumps + 1))
                visited.add(idx - 1)

            if not is_prime(number):
                continue
            # prime jump is accessible
            for teleport in teleportation[number].copy():
                q.append((teleport, nums[teleport], jumps + 1))
                visited.add(teleport)
                teleportation[number].remove(teleport)
        # actually unreachable
        return -1
