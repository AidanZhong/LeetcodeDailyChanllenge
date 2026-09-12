# Problem: Count Nodes Equal to Average of Subtree
# Topic: DFS
# Difficulty: Medium

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def sub_tree_sum_and_count(node):
            if not node:
                return (0, 0)
            left_sum, left_count = sub_tree_sum_and_count(node.left)
            right_sum, right_count = sub_tree_sum_and_count(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            if total_sum // total_count == node.val:
                nonlocal count
                count += 1
            return total_sum, total_count

        sub_tree_sum_and_count(root)
        return count