'''

    290. Word Pattern

'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        p_dict = {}
        s_dict = {}

        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in p_dict and s[i] not in s_dict:
                p_dict[pattern[i]] = s[i]
                s_dict[s[i]] = pattern[i]

            elif pattern[i] in p_dict and s[i] in s_dict:
                if p_dict[pattern[i]] != s[i] or s_dict[s[i]] != pattern[i]:
                    return False

            else:
                return False

        return True