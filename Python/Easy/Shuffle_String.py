'''

    1528. Shuffle String

'''

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [0] * len(indices)
        
        for i in range(len(indices)):
            shuffled[indices[i]] = s[i]
            
        s2 = ""
        return s2.join(shuffled)
