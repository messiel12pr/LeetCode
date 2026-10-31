'''

    1422. Maximum Score After Splitting a String

'''

class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for i in s:
            if i == '1':
                ones += 1

        if ones == len(s):
            return ones - 1

        res = 0
        zeroes = 0
        for i in s[:-1]:
            if i == '0':
                zeroes += 1

            else:
                ones -= 1

            res = max(res, zeroes + ones)
            
        if zeroes == len(s):
            return zeroes - 1

        return res

