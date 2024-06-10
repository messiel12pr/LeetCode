'''

    645. Set Mismatch

'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = [0 for _ in nums]
        res = [0, 0]

        for i in nums:
            cnt[i - 1] += 1

        for i in range(len(nums)):
            if cnt[i] == 2:
                res[0] = i + 1

            if cnt[i] == 0:
                res[1] = i + 1

        return res    