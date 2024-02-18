'''
    1876. Substrings of Size Three with Distinct Characters

    Solution:
'''

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = [0] * 26
        res = 0
        l = 0
        r = 0
        
        while r < len(s):
            count[ord(s[r]) - ord('a')] += 1

            if count[ord(s[r]) - ord('a')] > 1:
                while count[ord(s[r]) - ord('a')] > 1:
                    count[ord(s[l]) - ord('a')] -= 1
                    l += 1

            if r - l == 2:
                res += 1
                count[ord(s[l]) - ord('a')] -= 1
                l += 1
            
            r += 1

        return res