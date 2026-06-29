# Problem: Number of Substrings Containing All Three Characters
# Topic: Sliding window
# Difficulty: Medium

'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.



Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
Example 3:

Input: s = "abc"
Output: 1


Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_dict = {'a': 0, 'b': 0, 'c': 0}
        ans = 0
        l = 0
        r = 0
        n = len(s)
        while l <= r <= n:
            if char_dict['a'] > 0 and char_dict['b'] > 0 and char_dict['c'] > 0:
                ans += n - r + 1  # s[l..r-1] is valid, so s[l..r-1], s[l..r], ..., s[l..n-1] are all valid
                char_dict[s[l]] -= 1
                l += 1
            else:
                if r == n:
                    break
                char_dict[s[r]] += 1
                r += 1
        return ans


print(Solution().numberOfSubstrings(s="abcabc"))
