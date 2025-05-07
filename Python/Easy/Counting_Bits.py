'''

    338. Counting Bits

'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0, 1]
        factor = 2
        i = 2

        while i <= n:
            num = res[i-factor]
            if i > factor//2:
                num += 1

            res.append(num)

            if i == factor:
                factor *= 2
            i += 1

        if n < 2:
            return res[:n+1]
        return res