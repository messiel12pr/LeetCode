'''

  14. Longest Common Prefix

  Solution:

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = min(strs, key=len)
        R = len(pref)
        i = 0

        while(i < len(strs)):
            if R == 0:
                break

            if pref[0:R] != strs[i][0:R]:
                i = 0
                R -= 1
                
            else:
                i = i+1

        return pref[0:R]
