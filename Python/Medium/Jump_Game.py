'''

    55. Jump Game

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= last_idx - i:
                last_idx = i
        
        return last_idx == 0
