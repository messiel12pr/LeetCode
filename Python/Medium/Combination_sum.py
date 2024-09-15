'''

    39. Combination Sum

'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def rec(subset, i, curr_sum):
            if curr_sum == target:
                res.append(subset.copy())
                return

            elif curr_sum > target:
                return

            for n in range(i, len(candidates)):
                subset.append(candidates[n])
                rec(subset, n, curr_sum + candidates[n])
                subset.pop()

        rec([], 0, 0)
        return res