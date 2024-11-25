"""
1248. Count Number of Nice Subarrays
Medium
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
"""


def numberOfSubarrays(nums: list[int], k: int) -> int:
    count = 0
    odd_count = 0
    prefix_counts = {0: 1}

    for num in nums:
        odd_count += num % 2

        if odd_count - k in prefix_counts:
            count += prefix_counts[odd_count - k]

        prefix_counts[odd_count] = prefix_counts.get(odd_count, 0) + 1

    return count


print(numberOfSubarrays([1, 1, 2, 1, 1], 3))
print(numberOfSubarrays([2, 4, 6], 1))
print(numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))