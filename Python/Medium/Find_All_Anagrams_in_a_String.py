'''

    438. Find All Anagrams in a String

'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_s = [0 for i in range(26)]
        count_p = [0 for i in range(26)]
        for c in p:
            count_p[ord(c) - ord('a')] += 1

        l = 0
        res = []
        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            if (i - l) + 1 == len(p):
                if count_s == count_p:
                    res.append(l)
                count_s[ord(s[l]) - ord('a')] -= 1
                l += 1
        return res