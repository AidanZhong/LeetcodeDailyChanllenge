# Problem: Minimum Operations to Sort a String
# Topic: String
# Difficulty: Medium


class Solution:
    def minOperations(self, s: str) -> int:
        def already_sorted(s: str) -> bool:
            for i in range(1, len(s)):
                if s[i] < s[i - 1]:
                    return False
            return True

        if already_sorted(s):
            return 0

        if len(s) == 2:
            return -1

        def get_biggest_smallest_places(s: str):
            biggest = s[0]
            smallest = s[0]
            idx_dict = {'biggest': [0], 'smallest': [0]}
            for i in range(1, len(s)):
                if s[i] > biggest:
                    biggest = s[i]
                    idx_dict['biggest'] = [i]
                elif s[i] == biggest:
                    idx_dict['biggest'].append(i)
                if s[i] < smallest:
                    smallest = s[i]
                    idx_dict['smallest'] = [i]
                elif s[i] == smallest:
                    idx_dict['smallest'].append(i)
            return idx_dict

        idx_dict = get_biggest_smallest_places(s)

        if idx_dict['biggest'][-1] == len(s) - 1 or idx_dict['smallest'][0] == 0:
            return 1

        if idx_dict['biggest'] == [0] and idx_dict['smallest'] == [len(s) - 1]:
            return 3

        return 2


print(Solution().minOperations("dog"))
