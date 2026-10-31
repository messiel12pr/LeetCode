'''

    34. Find First and Last Position of Element in Sorted Array

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1]
