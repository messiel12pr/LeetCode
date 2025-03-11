'''

    383. Ransom Note

'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ctr = Counter(magazine)

        for c in ransomNote:
            if c not in ctr or ctr[c] == 0:
                return False

            ctr[c] -= 1

        return True