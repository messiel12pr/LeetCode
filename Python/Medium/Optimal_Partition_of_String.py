'''

    2405. Optimal Partition of String

'''

# Slower
class Solution:
    def partitionString(self, s: str) -> int:
        l, r = 0, 0
        res = 1

        while r < len(s):
            if s[r] in s[l:r]:
                l = r
                res += 1
            r += 1
        
        return res

# Optimal  
class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        res = 1

        for i in s:
            if i in seen:
                res += 1
                seen = set(i)

            else:
                seen.add(i)

        return res