# Problem: Longest Absolute File Path
# Topic: DFS
# Difficulty: Medium


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split("\n")
        n = len(lines)
        longest = 0
        stacks = [0] * (n + 1)  # the depth of current stack

        for i in range(n):
            stack_size = lines[i].count("\t")
            actual_name = lines[i].lstrip("\t")

            if stack_size == 0:
                stacks[stack_size] = len(actual_name)
            else:
                stacks[stack_size] = len(actual_name) + stacks[stack_size - 1] + 1

            if "." in actual_name:
                longest = max(longest, stacks[stack_size])
        return longest
