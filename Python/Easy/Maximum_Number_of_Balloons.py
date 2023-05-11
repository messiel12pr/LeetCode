'''

    1189. Maximum Number of Balloons

    Solution:

'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm = {'b': 0, 'a':0, 'l':0, 'o':0, 'n':0}
        for i in text:
            if i in hm:
                hm[i] += 1

        hm['l'] = int(hm['l']/2)
        hm['o'] = int(hm['o']/2)

        return min(hm.values())