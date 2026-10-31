'''

    33. Search in Rotated Sorted Array

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # current window sorted
            if nums[left] <= nums[right]:
                if nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1
                continue

            # left window sorted
            if nums[left] <= nums[mid]:
                if target in range(nums[left], nums[mid] + 1):
                    right = mid - 1

                else:
                    left = mid + 1
                continue

            # right window sorted
            if nums[mid] <= nums[right]:
                if target in range(nums[mid], nums[right] + 1):
                    left = mid + 1

                else:
                    right = mid - 1
                continue      

        return -1
