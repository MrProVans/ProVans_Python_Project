"""
718. Maximum Length of Repeated Subarray
Medium
Given two integer arrays nums1 and nums2,
return the maximum length of a subarray that appears in both arrays.
"""


def findLength(nums1: list[int], nums2: list[int]) -> int:
    n, m = len(nums1), len(nums2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    maxLength = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                maxLength = max(maxLength, dp[i][j])

    return maxLength


print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
print(findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))
print(findLength([1, 2, 3], [4, 5, 6]))
