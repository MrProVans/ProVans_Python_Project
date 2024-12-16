"""
96. Unique Binary Search Trees
Medium
Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.
"""


class Solution:
    def numTrees(self, n: int) -> int:
        from math import comb
        return comb(2 * n, n) // (n + 1)