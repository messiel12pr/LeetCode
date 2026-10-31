'''

    2348. Number of Zero-Filled Subarrays

'''

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total_sum = 0
        i = 0

        while i < len(nums):
            n = 0
            while i < len(nums) and nums[i] == 0:
                total_sum += n

                n += 1
                i += 1

            total_sum += n
            i += 1

        return total_sum 
