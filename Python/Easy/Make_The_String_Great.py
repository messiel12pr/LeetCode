"""

    1544. Make The String Great

    Solution:

"""

class Solution:
    def makeGood(self, s: str) -> str:
        l = list(s)
        i = 0
        
        while i<len(l)-1:
            if l[i] != l[i+1] and l[i].lower() == l[i+1].lower():
                del l[i]
                del l[i]
                if i != 0:
                    i -= 1
                continue

            i += 1

        s = ''.join(l)
        return s
