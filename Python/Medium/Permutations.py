'''

    46. Permutations

'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(subset, i):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for n in range(len(nums)):
                if nums[n] in subset:
                    continue
                subset.append(nums[n])
                rec(subset, i+1)
                subset.pop()

        rec([], 0)
        return res