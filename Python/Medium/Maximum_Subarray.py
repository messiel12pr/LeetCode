'''

    53. Maximum Subarray

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        curr_sum = 0
        for num in nums:
            if curr_sum <= 0:
                curr_sum = 0
            
            curr_sum += num
            res = max(res, curr_sum)
        
        return res

