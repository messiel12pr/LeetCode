'''

    896. Monotonic Array

'''

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec = False
        inc = False

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                dec = True

            if nums[i] > nums[i+1]:
                inc = True
            
            if dec and inc:
                return False

        return True