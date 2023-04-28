'''
    
    27. Remove Element

    Solution:

'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr_l = 0
        ptr_r = len(nums)-1

        while ptr_l <= ptr_r:
            if nums[ptr_l] == val and nums[ptr_r] != val:
                nums[ptr_l], nums[ptr_r] = nums[ptr_r], nums[ptr_l]
                ptr_l += 1
                ptr_r -= 1

            elif nums[ptr_r] == val:
                ptr_r -= 1

            else:
                ptr_l += 1

        return ptr_l 