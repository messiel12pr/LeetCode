'''

    345. Reverse Vowels of a String

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        res = [c for c in s]
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] in vowels and s[r] in vowels:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1

            if s[l] not in vowels:
                l += 1

            if s[r] not in vowels:
                r -= 1 

        return ''.join(res)