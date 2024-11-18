"""
1499. Max Value of Equation
Hard
You are given an array points containing the coordinates of points on a 2D plane,
 sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length.
  You are also given an integer k.
Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.
It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.
"""

from collections import deque


def findMaxValueOfEquation(points: list[list[int]], k: int):
    max_result = float('-inf')
    deque_window = deque()

    for x_j, y_j in points:
        while deque_window and x_j - deque_window[0][1] > k:
            deque_window.popleft()

        if deque_window:
            max_result = max(max_result, deque_window[0][0] + y_j + x_j)

        deque_window.append((y_j - x_j, x_j))

    return max_result


points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
print(findMaxValueOfEquation(points, k))