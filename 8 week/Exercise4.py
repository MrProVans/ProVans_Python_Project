"""
713. Subarray Product Less Than K
Medium
Given an array of integers nums and an integer k,
return the number of contiguous subarrays where the product
of all the elements in the subarray is strictly less than k.
"""


def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0

    product = 1
    start = 0
    count = 0

    for end in range(len(nums)):
        product *= nums[end]
        while product >= k:
            product //= nums[start]
            start += 1
        count += end - start + 1

    return count


print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(numSubarrayProductLessThanK([1, 2, 3], 0))
print(numSubarrayProductLessThanK([1, 2, 3], 7))
