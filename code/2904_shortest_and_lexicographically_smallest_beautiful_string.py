# Problem: Shortest and Lexicographically Smallest Beautiful String
# Topic: Sliding window
# Difficulty: Medium


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        sub = ""
        l, r = 0, 0
        count_of_one = 0
        while l <= r < len(s):
            if s[r] == '1':
                count_of_one += 1
            if count_of_one == k:
                while s[l] == '0':
                    l += 1
                temp_sub_string = s[l:r + 1]
                if (sub == "" or r - l + 1 < len(sub) or
                        r - l + 1 == len(sub) and temp_sub_string < sub):
                    sub = temp_sub_string
                count_of_one -= 1
                l += 1
            r += 1
        return sub


print(Solution().shortestBeautifulSubstring("100011001", 3))
