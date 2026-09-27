# Problem: Maximum Number of Non-Overlapping Substrings
# Topic: DFS
# Difficulty: Hard
from collections import defaultdict
from functools import cache


def get_total_len(l: list):
    total_len = 0
    for i in l:
        total_len += len(i)
    return total_len


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        char_indexes_dict = defaultdict(list)
        for i, char in enumerate(s):
            if len(char_indexes_dict[char]) > 1:
                char_indexes_dict[char][-1] = i
            else:
                char_indexes_dict[char].append(i)

        def get_next_available_index(i):
            # returns the exclusive end of the smallest valid substring starting at i,
            # or -1 if no valid substring starts at i
            right = char_indexes_dict[s[i]][-1]
            j = i
            while j <= right:
                first, last = char_indexes_dict[s[j]][0], char_indexes_dict[s[j]][-1]
                if first < i:
                    return -1  # s[j] leaks to the left of i -> impossible
                right = max(right, last)
                j += 1
            return right + 1

        @cache
        def dfs(i) -> tuple[int, list[str]]:
            # from i to the end of the string, the maximum number of non-overlapping substrings
            if i >= n:
                return 0, []
            maxi_number, substrings = 0, []

            # trying to use the current character as the start of a substring
            next_available_index = get_next_available_index(i)
            if next_available_index != -1:
                temp_maxi, temp_substrings = dfs(next_available_index)
                temp_maxi += 1
                temp_substrings = [s[i:next_available_index]] + temp_substrings
                if temp_maxi > maxi_number:
                    maxi_number, substrings = temp_maxi, temp_substrings
                elif temp_maxi == maxi_number and get_total_len(temp_substrings) < get_total_len(substrings):
                    substrings = temp_substrings

            # not using
            temp_maxi, temp_substrings = dfs(i + 1)
            if temp_maxi > maxi_number:
                maxi_number, substrings = temp_maxi, temp_substrings
            elif temp_maxi == maxi_number and get_total_len(temp_substrings) < get_total_len(substrings):
                substrings = temp_substrings
            return maxi_number, substrings

        return dfs(0)[1]


print(Solution().maxNumOfSubstrings("adefaddaccc"))
