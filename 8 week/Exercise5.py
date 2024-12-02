"""
658. Find K Closest Elements
Medium
Given a sorted integer array arr, two integers k and x,
 return the k closest integers to x in the array.
 The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
"""


def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    left, right = left - 1, left

    while k > 0:
        if left < 0:
            right += 1
        elif right >= len(arr):
            left -= 1
        elif abs(arr[left] - x) <= abs(arr[right] - x):
            left -= 1
        else:
            right += 1
        k -= 1

    return sorted(arr[left + 1:right])


print(findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(findClosestElements([1, 2, 3, 4, 5], 4, -1))
print(findClosestElements([1, 1, 1, 10, 10, 10], 1, 9))
