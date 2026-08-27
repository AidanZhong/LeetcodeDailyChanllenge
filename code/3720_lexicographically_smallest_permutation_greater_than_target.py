# Problem: Lexicographically Smallest Permutation Greater Than Target
# Topic: Greedy
# Difficulty: Medium
from collections import defaultdict


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        letter_dict = [0] * 26
        for i in s:
            letter_dict[ord(i) - ord('a')] += 1

        def could_form(target_idx):
            # form the biggest string
            max_str = ''
            for x in range(25, -1, -1):
                max_str += chr(x + ord('a')) * letter_dict[x]
            return max_str > target[target_idx:]

        def form_smallest():
            smallest = ''
            for i in range(26):
                smallest += chr(i + ord('a')) * letter_dict[i]
            return smallest

        ans = ''
        flag_of_greater = False
        for idx, t in enumerate(target):
            t_idx = ord(t) - ord('a')
            if flag_of_greater:
                return ans + form_smallest()
            else:
                letter_dict[t_idx] -= 1
                if letter_dict[t_idx] >= 0 and could_form(idx + 1):
                    ans += t
                else:
                    letter_dict[t_idx] += 1
                    # find the next letter
                    for offset in range(1, 26):
                        next_char = t_idx + offset
                        if next_char < 26 and letter_dict[next_char] > 0:
                            break
                    else:
                        return ''
                    letter_dict[next_char] -= 1
                    ans += chr(next_char + ord('a'))
                    flag_of_greater = True

        return ans if flag_of_greater else ''


print(Solution().lexGreaterPermutation(s='aabb', target='abba'))
