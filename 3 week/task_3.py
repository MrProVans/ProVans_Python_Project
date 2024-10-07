"""16. 3Sum Closest
Medium
Given an integer array nums of length n and an integer target,
 find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution."""


def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum == target:
                return current_sum
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum


print(threeSumClosest([-1, 2, 1, -4], 1))
print(threeSumClosest([0, 0, 0], 1))