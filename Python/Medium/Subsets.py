'''

    78. Subsets

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(i, subset):
            res.append(subset.copy())
            
            for n in range(i, len(nums)):
                subset.append(nums[n])
                rec(n + 1, subset)
                subset.pop()

        rec(0, [])
        return res  
