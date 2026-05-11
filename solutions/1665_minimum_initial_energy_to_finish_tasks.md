# 1665. Minimum Initial Energy to Finish Tasks

- **Difficulty:** Hard
- **Topic:** Greedy

https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description/

## Approach

Though they tagged the problem as hard, it's actually quite easy to solve if you think about it.

The sequence of task manipulation is the key. Some task need a lot of energy to start but actually cost very little
energy to finish. Some of them need the same amount of energy to start and finish. We call this the "Energy gap"

Since we need the minimum energy to finish all tasks, we want the minimum energy left after finishing all tasks. 
That is to say we want the task with the minimum energy gap to be done last. Try to do the task with the maximum
energy gap first so we can have more remaining energy for the remaining tasks instead of wasting them.

Then the problem becomes a simple greedy problem. All we need is sort the tasks array by the energy gap. Then simulate the process
and keep track of the needed energy.

## Complexity

- **Time:** O(n log n)
  - Sorting tasks by energy gap: O(n log n)
  - Single pass through sorted tasks: O(n)
- **Space:** O(n)
  - `sorted_tasks` stores a new sorted copy of the input array

## Code

[View solution](../code/1665_minimum_initial_energy_to_finish_tasks.py)
