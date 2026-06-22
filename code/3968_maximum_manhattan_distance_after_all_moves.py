# Problem: Maximum Manhattan Distance After All Moves
# Topic: simulation
# Difficulty: Medium
'''
You are given a string moves consisting of the characters 'U', 'D', 'L', 'R', and '_'.

Starting from the origin (0, 0), each character represents one move on a 2D plane:

'U': Move up by 1 unit.
'D': Move down by 1 unit.
'L': Move left by 1 unit.
'R': Move right by 1 unit.
'_': Can be independently replaced with any one of 'U', 'D', 'L', or 'R'.
Return the maximum Manhattan distance from the origin that can be achieved after all moves have been performed.
'''


class Solution:
    def maxDistance(self, moves: str) -> int:
        x, y = 0, 0
        count = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
            else:
                count += 1
        return abs(x) + abs(y) + count