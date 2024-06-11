'''

    1496. Path Crossing

'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        hm = {'N': -1, 'S': 1, 'E': 1, 'W': -1}
        pnt = (0, 0)
        curr_path = set()
        curr_path.add(pnt)

        for c in path:
            i = hm[c]

            if c == 'N' or c == 'S':
                pnt = (pnt[0], pnt[1] + i)

            else:
                pnt = (pnt[0] + i, pnt[1])

            if pnt in curr_path:
                return True

            curr_path.add(pnt)

        return False