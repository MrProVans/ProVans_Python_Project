"""
889. Construct Binary Tree from Preorder and Postorder Traversal
Medium
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree
of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
If there exist multiple answers, you can return any of them.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        postorder_index = {value: i for i, value in enumerate(postorder)}

        def build_tree(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            if pre_start == pre_end:
                return root

            left_root_val = preorder[pre_start + 1]

            left_root_post_idx = postorder_index[left_root_val]

            left_subtree_size = left_root_post_idx - post_start + 1

            root.left = build_tree(pre_start + 1, pre_start + left_subtree_size, post_start, left_root_post_idx)
            root.right = build_tree(pre_start + left_subtree_size + 1, pre_end, left_root_post_idx + 1, post_end - 1)

            return root

        return build_tree(0, len(preorder) - 1, 0, len(postorder) - 1)