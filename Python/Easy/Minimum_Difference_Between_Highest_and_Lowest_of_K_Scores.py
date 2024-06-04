'''

    1984. Minimum Difference Between Highest and Lowest of K Scores

'''

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k - 1
        res = float('inf')
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        return res