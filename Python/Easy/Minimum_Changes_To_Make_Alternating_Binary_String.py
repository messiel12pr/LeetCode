'''

    1758. Minimum Changes To Make Alternating Binary String

'''

class Solution:
    def minOperations(self, s: str) -> int:
        cnt = {'0':[0, 0],
               '1':[0, 0]}

        for i in range(len(s)):
            cnt[s[i]][i % 2] += 1

        return len(s) - max(cnt['0'][0] + cnt['1'][1], cnt['0'][1] + cnt['1'][0])