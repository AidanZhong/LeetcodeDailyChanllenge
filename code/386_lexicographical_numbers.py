# Problem: Lexicographical Numbers
# Topic: DFS
# Difficulty: Medium

'''

'''

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(i):
            if i <= n:
                ans.append(i)
            else:
                return
            # try to add 0 to the end
            if i * 10 <= n:
                dfs(i * 10)
            # try to plus 1
            if str(i)[-1] != '9':
                dfs(i + 1)

        dfs(1)
        return ans
