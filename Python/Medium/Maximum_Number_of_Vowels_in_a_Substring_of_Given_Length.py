'''
    1456. Maximum Number of Vowels in a Substring of Given Length

    Solution:
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowls = ['a', 'e', 'i', 'o', 'u']
        l, res, ctr = 0, 0, 0
        
        for r in range(len(s)):
            if s[r] in vowls:
                ctr += 1
            
            if r - l + 1 == k and ctr != k:
                res = max(res, ctr)
                if s[l] in vowls:
                    ctr -= 1
                l += 1

            if ctr == k:
                return ctr

        return res