'''

    1913. Maximum Product Difference Between Two Pairs

'''

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        w = 0
        x = 0
        y = float("inf")
        z = float("inf")

        for i in nums:
            if i > w:
                x = w
                w = i
            
            elif i > x:
                x = i

            if i < y:
                z = y
                y = i

            elif i < z:
                z = i

        return w*x - y*z