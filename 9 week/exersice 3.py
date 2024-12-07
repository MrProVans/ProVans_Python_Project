"""
863. All Nodes Distance K in Binary Tree
Medium
Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.
"""


from collections import deque, defaultdict
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def map_parents(node, parent):
            if not node:
                return
            if parent:
                parents[node] = parent
            map_parents(node.left, node)
            map_parents(node.right, node)

        parents = {}
        map_parents(root, None)

        queue = deque([(target, 0)])
        visited = set()
        visited.add(target)
        result = []

        while queue:
            current_node, distance = queue.popleft()

            if distance == k:
                result.extend(node.val for node, _ in queue)
                result.append(current_node.val)
                break

            for neighbor in (current_node.left, current_node.right, parents.get(current_node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return result