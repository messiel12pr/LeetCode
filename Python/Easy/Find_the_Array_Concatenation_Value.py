'''

    2562. Find the Array Concatenation Value 

    Solution:

'''

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = sum = 0
        r = len(nums)-1
        s = ''

        while l < r:
            s = str(nums[l]) + str(nums[r])
            sum += int(s)

            del nums[r]
            del nums[l]

            s = ''
            l = 0
            r = len(nums)-1
            
        if len(nums) == 1:
            sum += nums[0]

        return sum
