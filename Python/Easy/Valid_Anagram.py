'''

    242. Valid Anagram

    Solution:

'''

def populate_dict(s: string, hm: dict):
    for i in s:
        if hm.get(i) == None:
            hm[i] = 1

        else:
            hm[i] += 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_1, dict_2 = {}

        populate_dict(s, dict_1)
        populate_dict(t, dict_2)

        return dict_1.items() == dict_2.items()