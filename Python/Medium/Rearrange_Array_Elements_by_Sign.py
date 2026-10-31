'''

    2149. Rearrange Array Elements by Sign

'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        positive = 0
        negative = 0

        for i in range(len(nums)):
            while positive < len(nums) and nums[positive] < 0:
                positive += 1

            while negative < len(nums) and nums[negative] > 0:
                negative += 1
                negative

            if positive < len(nums):
                res.append(nums[positive])
                positive += 1

            if negative < len(nums):
                res.append(nums[negative])
                negative += 1

        return res
