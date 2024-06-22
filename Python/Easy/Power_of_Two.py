'''

    231. Power of Two

'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cnt = 0
        bits = n
        
        while bits:
            cnt += int(bits & 1)
            bits >>= 1
            if cnt > 1:
                return False

        return n != 0