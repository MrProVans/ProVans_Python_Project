"""
814. Binary Tree Pruning
Medium
Given the root of a binary tree, return the same tree where every subtree (of the given tree)
not containing a 1 has been removed.
A subtree of a node node is node plus every node that is a descendant of node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and not root.left and not root.right:
            return None

        return root