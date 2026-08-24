# Problem: Sum Game
# Topic: Math
# Difficulty: Medium


class Solution:
    def sumGame(self, num: str) -> bool:
        first_half = {"s": 0, "?": 0}
        second_half = {"s": 0, "?": 0}

        for i in range(len(num)):
            if i < len(num) // 2:
                if num[i] == "?":
                    first_half["?"] += 1
                else:
                    first_half["s"] += int(num[i])
            else:
                if num[i] == "?":
                    second_half["?"] += 1
                else:
                    second_half["s"] += int(num[i])

        s_question_mark = first_half["?"] + second_half["?"]
        if s_question_mark % 2 == 1:
            return True
        if s_question_mark == 0:
            return first_half["s"] != second_half["s"]
        if s_question_mark == 2:
            if first_half['?'] == 1:
                return first_half['s'] != second_half['s']
        return first_half['s'] - second_half['s'] != (second_half['?'] - first_half['?']) * 9 // 2


print(Solution().sumGame("81??"))
