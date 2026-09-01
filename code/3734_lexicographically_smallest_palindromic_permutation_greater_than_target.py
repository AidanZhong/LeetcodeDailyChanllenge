# Problem: Lexicographically Smallest Palindromic Permutation Greater Than Target
# Topic: Greedy
# Difficulty: Hard


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        letter_dict = [0] * 26
        for i in s:
            letter_dict[ord(i) - ord('a')] += 1

        centra_char = ''
        if len(s) % 2 == 1:
            for i in range(26):
                if letter_dict[i] % 2 == 1:
                    centra_char = chr(i + ord('a'))
                    letter_dict[i] -= 1
            if not centra_char:
                return ''

        def could_form(cur):
            # form the biggest string
            max_str = ''
            for x in range(25, -1, -1):
                max_str += chr(x + ord('a')) * (letter_dict[x] // 2)
            max_str = cur + max_str + centra_char + max_str[::-1] + cur[::-1]
            return max_str > target

        def form_smallest(cur):
            smallest = ''
            for x in range(26):
                smallest += chr(i + ord('a')) * (letter_dict[x] // 2)
            return cur + smallest + centra_char + smallest[::-1] + cur[::-1]

        ans = ''
        flag_of_greater = False
        for idx, t in enumerate(target[:len(target) // 2]):
            t_idx = ord(t) - ord('a')
            if flag_of_greater:
                return form_smallest(ans)
            else:
                if letter_dict[t_idx] >= 2 and could_form(ans):
                    letter_dict[t_idx] -= 2
                    ans += t
                else:
                    # find the next letter
                    for offset in range(1, 26):
                        next_char = t_idx + offset
                        if next_char < 26 and letter_dict[next_char] > 0:
                            break
                    else:
                        return ''
                    letter_dict[next_char] -= 2
                    ans += chr(next_char + ord('a'))
                    flag_of_greater = True
        return ans if flag_of_greater else ''


print(Solution().lexPalindromicPermutation('baba', 'abba'))
