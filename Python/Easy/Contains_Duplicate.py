'''

    217. Contains Duplicate

    Solution

'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}

        for i in nums:
            if hm.get(i) == None:
                hm[i] = 1

            else:
                hm[i] += 1

            if hm.get(i) > 1:
                return True

        return False