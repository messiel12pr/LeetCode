'''

    205. Isomorphic Strings

    Solution

'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ptr = 0
        hm = {}

        while ptr < len(s):
            if s[ptr] not in hm:
                if t[ptr] not in hm.values():
                    hm[s[ptr]] = t[ptr]

                else:
                    return False

            elif s[ptr] in hm and hm[s[ptr]] != t[ptr]:
                return False

            ptr += 1

        return True
