'''

    42. Trapping Rain Water

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []

        m = height[0]
        for i in range(0, len(height)):
            m = max(m, height[i])
            left.append(m)
        
        m = height[-1]
        for i in range(len(height)-1, -1, -1):
            m = max(m, height[i])
            right.insert(0, m)

        res = 0
        for i in range(len(height)):
            curr = min(left[i], right[i]) - height[i]
            if curr > 0:
                res += curr

        return res