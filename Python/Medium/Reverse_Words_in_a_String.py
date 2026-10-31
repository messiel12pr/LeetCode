'''

    151. Reverse Words in a String

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        l = len(s) - 1
        r = len(s) - 1
        reverse = []

        while l >= 0 and r >= 0:
            if s[r] != ' ':
                l = r
                while l > 0 and s[l] != ' ':
                    l -= 1

                if s[l] == ' ':
                    reverse.append(s[l + 1:r + 1])
                    
                else:
                    reverse.append(s[l:r + 1])

                reverse.append(' ')
                r = l

            r -= 1

        reverse.pop()
        return ''.join(reverse)

