'''

    386. Find the Difference

'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        new_str = s + t
        val = 0

        for c in new_str:
            val ^= ord(c)

        return chr(val)