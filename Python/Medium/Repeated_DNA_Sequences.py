'''

    187. Repeated DNA Sequences

'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = []
        l = 0

        for i in range(len(s)):
            if (i - l) + 1 != 10:
                continue

            if s[l:i+1] in seen:
                res.append(s[l:i+1])

            else:
                seen.add(s[l:i+1])

            l += 1

        return set(res)