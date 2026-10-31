'''

    374. Guess Number Higher or Lower

'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0

        while low <= n:
            middle = (low + n)//2

            if guess(middle) == 0:
                return middle

            elif guess(middle) > 0:
                low = middle + 1
            
            else:
                n = middle - 1
