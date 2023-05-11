'''

    724. Find Pivot Index

    Solution:

'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        list_sum = sum(nums)

        for i in range(len(nums)):
            right_sum = list_sum - nums[i] - left_sum          
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1