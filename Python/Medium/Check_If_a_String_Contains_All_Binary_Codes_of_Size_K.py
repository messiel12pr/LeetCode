'''

    1461. Check If a String Contains All Binary Codes of Size K

'''

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        j = k
        for i in range(len(s) - k + 1):
            codes.add(s[i:j])
            j += 1

        return len(codes) == pow(2, k)