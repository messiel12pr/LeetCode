'''

    2870. Minimum Number of Operations to Make Array Empty

'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0

        for k, v in cnt.items():
            if v == 1:
                return -1

            x = ceil(v//3) - 1
            y = (v - (x * 3))//2
            res += x + y

        return res