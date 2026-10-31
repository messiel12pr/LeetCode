'''

    229. Majority Element II

'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = defaultdict(int)

        for i in nums:
            cnt[i] += 1

            if len(cnt) > 2:
                copy = cnt.copy()
                for k, v in cnt.items():
                    cnt[k] = v - 1
                    if cnt[k] == -1:
                        copy.pop(k)
                cnt = copy

        res = []
        for k, v in cnt.items():
            if v > len(nums)/3:
                res.append(k)

        return res
