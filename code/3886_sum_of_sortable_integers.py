# Problem: Sum of Sortable Integers
# Topic: Math
# Difficulty: Hard

def check_circular_sorted(nums: list[int]) -> tuple[bool, int, int]:
    if len(nums) <= 1:
        return True, nums[0], nums[0]

    cur = 1
    mini = nums[0]
    maxi = nums[-1]
    minimal_flag = False
    while cur < len(nums):
        if nums[cur] < nums[cur - 1]:
            if minimal_flag:
                return False, -1, -1
            minimal_flag = True
            mini = nums[cur]
            maxi = nums[cur - 1]
        cur += 1
    if minimal_flag and nums[-1] > nums[0]:
        return False, -1, -1
    return True, mini, maxi


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for k in range(1, n + 1):
            if n % k == 0:
                is_sortable = True
                prev_mini, prev_maxi = -1, -1
                for i in range(n // k):
                    start = i * k
                    end = start + k
                    subarray = nums[start:end]
                    is_circular_sorted, min_val, max_val = check_circular_sorted(subarray)
                    if not is_circular_sorted:
                        is_sortable = False
                        break
                    if min_val < prev_maxi:
                        is_sortable = False
                        break
                    prev_mini, prev_maxi = min_val, max_val
                if is_sortable:
                    ans += k
        return ans


print(Solution().sortableIntegers([3, 1, 2]))
