# Problem: Number of Paths with Max Score
# Topic: Dynamic programming
# Difficulty: Hard

'''
You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].



Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]
Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]
Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]


Constraints:

2 <= board.length == board[i].length <= 100
'''

from functools import cache
from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10 ** 9 + 7
        board[n - 1] = board[n - 1].replace('S', '0')

        @cache
        def dp(i, j):
            '''
            Calculate the max score and number of paths from cell (i, j)
            :param i: row
            :param j: col
            :return: max score, number of paths
            '''
            if i < 0 or j < 0 or i >= n or j >= n:
                return [0, 0]  # no path

            if (i, j) == (0, 0):
                return [0, 1]
            if board[i][j] == 'X':
                return [0, 0]  # no path

            adj = [dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)]
            adj.sort(reverse=True)

            if adj[0][0] > adj[1][0] >= adj[2][0]:
                return [adj[0][0] + int(board[i][j]), adj[0][1] % MOD] if adj[0][1] != 0 else [0, 0]
            elif adj[0][0] == adj[1][0] > adj[2][0]:
                return [adj[0][0] + int(board[i][j]), (adj[0][1] + adj[1][1]) % MOD] if adj[0][1] != 0 else [0, 0]
            else:
                return [adj[0][0] + int(board[i][j]), (adj[0][1] + adj[1][1] + adj[2][1]) % MOD] if adj[0][1] != 0 else [0, 0]

        # for i in range(n):
        #     for j in range(n):
        #         print(f'dp({i}, {j}) = {dp(i, j)}')
        return dp(n - 1, n - 1)


print(Solution().pathsWithMaxScore(["E23", "2X2", "12S"]))
# print(Solution().pathsWithMaxScore(["E11", "XXX", "11S"]))
