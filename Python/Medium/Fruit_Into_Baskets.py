'''
    904. Fruit Into Baskets

    Solution:
'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = [0] * len(fruits)
        l, r = 0, 0
        ctr = 0
        res = 1

        while r < len(fruits):
            while ctr > 2:
                if freq[fruits[l]] != 0:
                    freq[fruits[l]] -= 1
                    
                if freq[fruits[l]] == 0:
                    ctr -= 1

                l += 1

            if freq[fruits[r]] == 0:
                ctr += 1

            if ctr <= 2:
                res = max(res, r - l + 1)

            freq[fruits[r]] += 1
            r += 1

        return res