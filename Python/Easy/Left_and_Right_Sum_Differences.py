'''

    2574. Left and Right Sum Differences

'''

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre_sum = [nums[0]]
        res = []

        for i in range(1, len(nums)):
            pre_sum.append(pre_sum[i - 1] + nums[i])
        
        pre_sum.insert(0, 0)
        pre_sum.append(0)

        for i in range(1, len(pre_sum) - 1):
            res.append(abs(pre_sum[-2] - pre_sum[i-1] - pre_sum[i]))

        return res