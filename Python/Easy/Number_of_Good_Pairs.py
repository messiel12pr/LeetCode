'''

    1512. Number of Good Pairs

'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        res = 0

        for i in range(len(nums) - 1, -1, -1):
            hm[nums[i]] += 1
            if hm[nums[i]] > 1:
                res += hm[nums[i]] - 1

        return res
