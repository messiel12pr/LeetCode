'''
    209. Minimum Size Subarray Sum

    Solution:
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, curr_sum = 0, 0
        res = float('inf')

        while r < len(nums):
            curr_sum += nums[r]
            while curr_sum >= target:
                res = min(res, r - l + 1)
                curr_sum -= nums[l]
                l += 1

            r += 1

        return res if res != float('inf') else 0