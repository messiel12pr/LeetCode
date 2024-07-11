'''

    153. Find Minimum in Rotated Sorted Array

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("inf")

        while l <= r:
            m = (r + l)//2
            res = min(res, nums[l], nums[m])

            if nums[m] >= nums[l]:
                l = m + 1

            else:
                r = m - 1
        
        return res