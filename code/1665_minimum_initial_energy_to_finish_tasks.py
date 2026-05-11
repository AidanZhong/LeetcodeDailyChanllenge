# Problem: Minimum Initial Energy to Finish Tasks
# Topic: Greedy
# Difficulty: Hard

'''
You are given an array tasks where tasks[i] = [actuali, minimumi]:

actuali is the actual amount of energy you spend to finish the ith task.
minimumi is the minimum amount of energy you require to begin the ith task.
For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

You can finish the tasks in any order you like.

Return the minimum initial amount of energy you will need to finish all the tasks.
'''
from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        sorted_tasks = sorted(tasks, key=lambda x: x[1] - x[0], reverse=True)
        minimum_energy = 0
        current_energy = 0
        for task in sorted_tasks:
            if current_energy < task[1]:
                offset = task[1] - current_energy
                minimum_energy += offset
                current_energy = task[1] - task[0]  # after consume
            else:
                current_energy -= task[0]
        return minimum_energy


# print(Solution().minimumEffort(tasks=[[1, 2], [2, 4], [4, 8]]))
# print(Solution().minimumEffort(tasks=[[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]))
print(Solution().minimumEffort(tasks=[[1, 2], [1, 7], [2, 3], [5, 9], [2, 2]]))
