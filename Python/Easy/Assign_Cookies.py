'''

    455. Assign Cookies

'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        j, i = 0, 0

        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                res += 1
                j += 1
                i += 1

            else:
                j += 1

        return res