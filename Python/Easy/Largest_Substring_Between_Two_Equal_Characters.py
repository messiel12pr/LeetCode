'''

    1624. Largest Substring Between Two Equal Characters

'''

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        idxs = defaultdict(list)
        for i in range(len(s)):
            if s[i] not in idxs:
                idxs[s[i]].append(i + 1)

        for i in range(len(s) - 1, 0, -1):
            if len(idxs[s[i]]) == 1:
                res = max(res, i - idxs[s[i]][0])
                idxs[s[i]].append(i)

        return res