'''

    2001. Number of Pairs of Interchangeable Rectangles

'''

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hm = {}
        res = 0

        for i in range(len(rectangles)-1, -1, -1):
            ratio = rectangles[i][0]/rectangles[i][1]

            if ratio in hm and hm[ratio] == 1:
                res += 1

            elif ratio in hm and hm[ratio] > 1:
                res += hm[ratio]

            else:
                hm[ratio] = 0

            hm[ratio] += 1

        return res