"""
95. Unique Binary Search Trees II
Medium
Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build_trees(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = build_trees(start, i - 1)
                right_trees = build_trees(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)

            return all_trees

        return build_trees(1, n)