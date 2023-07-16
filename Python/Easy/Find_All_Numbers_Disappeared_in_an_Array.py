'''

    448. Find All Numbers Disappeared in an Array

    Solution:

'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        res = []

        while i < len(nums):
            if nums[i] > 0:
                if nums[nums[i]-1] != nums[i] and nums[nums[i]-1] >= 0:
                    var = nums[nums[i]-1]
                    nums[nums[i]-1] = -1 * nums[i]
                    nums [i] = var

                else:
                    if nums[i]-1 != i:
                        nums[i] = 0
                    i += 1

            else:
                i += 1

        for i in range(len(nums)):
            if abs(nums[i]) != i+1:
                res.append(i+1)

        return res