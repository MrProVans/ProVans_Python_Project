"""
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
Medium
You are given an array of integers arr and an integer target.
You have to find two non-overlapping sub-arrays of arr each with a sum equal target.
 There can be multiple answers so you have to find an answer where the sum of the
  lengths of the two sub-arrays is minimum.
Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.
"""


def minSumOfLengths(arr: list[int], target: int):
    n = len(arr)
    min_length = [float('inf')] * n
    current_sum = 0
    start = 0
    result = float('inf')

    for end in range(n):
        current_sum += arr[end]

        while current_sum > target:
            current_sum -= arr[start]
            start += 1

        if current_sum == target:
            length = end - start + 1
            if start > 0:
                result = min(result, length + min_length[start - 1])
            min_length[end] = min(min_length[end - 1], length) if end > 0 else length
        else:
            min_length[end] = min_length[end - 1] if end > 0 else float('inf')

    return result if result != float('inf') else -1


print(minSumOfLengths([3, 2, 2, 4, 3], 3))
print(minSumOfLengths([7, 3, 4, 7], 7))
print(minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6))