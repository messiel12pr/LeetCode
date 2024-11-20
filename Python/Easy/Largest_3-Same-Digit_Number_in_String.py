'''

    2264. Largest 3-Same-Digit Number in String

'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = [0 for x in range(10)]
        num += '-1'
        l = 0

        for i in range(len(num)-1):
            if (i - l) + 1 == 3:
                nums[int(num[i])] = 1
                l = i + 1

            if num[i] != num[i+1]:
                l = i + 1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 1:
                return str(i)*3

        return ''