# Problem: Kth Smallest Amount With Single Denomination Combination
# Topic: Number Theory
# Difficulty: Hard
from typing import List
from math import lcm


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        l = k
        r = coins[0] * k

        def count(x):
            n = len(coins)
            ans = 0
            for mask in range(1, 1 << n):
                cur_lcm = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        cur_lcm = lcm(cur_lcm, coins[i])
                        bits += 1
                        if cur_lcm > x:
                            break
                if cur_lcm > x:
                    continue
                if bits % 2 == 1:
                    ans += x // cur_lcm
                else:
                    ans -= x // cur_lcm
            return ans

        while l < r:
            mid = (l + r) // 2
            c = count(mid)
            if c < k:
                l = mid + 1
            else:
                r = mid
        return l
