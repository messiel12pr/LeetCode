'''

    213. House Robber II

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def solution(nums):
            if len(nums) <= 2:
                return max(nums)

            dp = [nums[0], max(nums[0], nums[1])]
            for i in range(2, len(nums)):
                dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))
            return dp[-1]

        return max(solution(nums[:-1]), solution(nums[1:]))
