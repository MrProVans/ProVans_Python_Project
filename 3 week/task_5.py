"""33. Search in Rotated Sorted Array
Medium
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown
 pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ...,
 nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might
  be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target
 if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity."""


def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Если нашли целевой элемент
        if nums[mid] == target:
            return mid

        # Проверяем, какая часть отсортирована
        if nums[left] <= nums[mid]:  # Левая часть отсортирована
            if nums[left] <= target < nums[mid]:  # Проверяем, лежит ли target в левой части
                right = mid - 1
            else:
                left = mid + 1
        else:  # Правая часть отсортирована
            if nums[mid] < target <= nums[right]:  # Проверяем, лежит ли target в правой части
                left = mid + 1
            else:
                right = mid - 1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([1], 0))