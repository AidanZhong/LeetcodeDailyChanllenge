# Problem: First Unique Character in a String
# Topic: Hashset
# Difficulty: Easy


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        visited = set()
        for idx, i in enumerate(s):
            if i not in visited:
                char_dict[i] = idx
                visited.add(i)
            elif i in char_dict:
                char_dict.pop(i)
        if not char_dict:
            return -1
        char_list = sorted(char_dict.items(), key=lambda x: x[1])
        return char_list[0][1]


# print(Solution().firstUniqChar(s="leetcode"))
print(Solution().firstUniqChar("aadadaad"))
