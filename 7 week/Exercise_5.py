"""
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
Medium
Given an array of integers arr and two integers k and threshold,
 return the number of sub-arrays of size k and average greater than or equal to threshold.
"""


def numOfSubarrays(arr: list[int], k: int, threshold: int) -> int:
    target = threshold * k
    current_sum = sum(arr[:k])
    count = 0

    if current_sum >= target:
        count += 1

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        if current_sum >= target:
            count += 1

    return count


print(numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))
print(numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))
print(numOfSubarrays([1,1,1,1,1], 1, 1))