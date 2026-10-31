'''

    90. Subsets II

'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def rec(i, subset):
            res.append(tuple(subset.copy()))
            
            for n in range(i, len(nums)):
                subset.append(nums[n])
                rec(n + 1, subset)
                subset.pop()

        rec(0, [])
        return set(res)       
