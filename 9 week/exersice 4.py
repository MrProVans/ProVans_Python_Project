"""
865. Smallest Subtree with all the Deepest Nodes
Medium
Given the root of a binary tree, the depth of each node is the shortest distance to the root.
Return the smallest subtree such that it contains all the deepest nodes in the original tree.
A node is called the deepest if it has the largest depth possible among any node in the entire tree.
The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find_depth_and_lca(node):
            if not node:
                return (0, None)

            # Recursively find the depth and LCA of the left and right subtrees
            left_depth, left_lca = find_depth_and_lca(node.left)
            right_depth, right_lca = find_depth_and_lca(node.right)

            # If left and right subtrees are at the same depth, then this node is the LCA of deepest nodes
            if left_depth == right_depth:
                return (left_depth + 1, node)
            # If left subtree is deeper, the LCA is in the left subtree
            elif left_depth > right_depth:
                return (left_depth + 1, left_lca)
            # If right subtree is deeper, the LCA is in the right subtree
            else:
                return (right_depth + 1, right_lca)

        # Step 2: Start the recursion from the root and return the LCA of the deepest nodes
        _, lca = find_depth_and_lca(root)
        return lca