"""
99. Recover Binary Search Tree
Medium
You are given the root of a binary search tree (BST),
where the values of exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """Do not return anything, modify root in-place instead."""
        first, second, prev = None, None, TreeNode(float('-inf'))

        def inorder(node):
            nonlocal first, second, prev
            if not node:
                return

            inorder(node.left)

            if not first and prev.val > node.val:
                first = prev
            if first and prev.val > node.val:
                second = node

            prev = node

            inorder(node.right)

        inorder(root)

        if first and second:
            first.val, second.val = second.val, first.val