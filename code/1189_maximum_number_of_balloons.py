# Problem: Maximum number of balloons
# Topic: hash set
# Difficulty: easy

'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
'''
from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_dict = defaultdict(int)

        for i in text:
            if i in "balloon":
                char_dict[i] += 1
        ans = min(char_dict["b"], char_dict["a"], char_dict["l"] // 2, char_dict["o"] // 2, char_dict["n"])
        return ans
