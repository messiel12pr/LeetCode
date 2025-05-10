'''

    1752. Check if Array Is Sorted and Rotated

'''

class Solution:
    def check(self, nums: List[int]) -> bool:
        m = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i] and m == 0:
                m = min(nums[:i])

            elif nums[i-1] > nums[i]:
                return False

            if m != 0 and nums[i] > m:
                return False

        return True