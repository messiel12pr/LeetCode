'''

    198. House Robber

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        arr = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            curr_max = max(nums[i] + arr[i - 2], arr[i - 1])
            arr.append(curr_max)

        print(arr)
        return arr[-1]
