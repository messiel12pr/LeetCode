'''

    2640. Find the Score of All Prefixes of an Array

'''

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        conver = [nums[0] * 2]
        m = nums[0]

        for i in range(1, len(nums)):
            m = max(m, nums[i])
            conver.append(conver[i - 1] + nums[i] + m)

        return conver