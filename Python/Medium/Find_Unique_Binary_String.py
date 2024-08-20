'''

    1980. Find Unique Binary String

'''

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ints = [int(n, 2) for n in nums]
        n = len(nums[0])
        res = ''

        for i in range(2**n):
            if i not in ints:
                return f'{i:0{n}b}'