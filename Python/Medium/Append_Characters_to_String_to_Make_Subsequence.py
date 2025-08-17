'''

    2486. Append Characters to String to Make Subsequence

'''

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for c in s:
            if i == len(t):
                return 0

            if c == t[i]:
                i += 1
        
        return len(t) - i