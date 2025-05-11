'''

    1002. Find Common Characters

'''

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        frequencies = []
        res = []

        for w in words:
            frequencies.append(Counter(w))

        for c in 'abcdefghijklmnopqrstuvwxyz':
            min_freq = float("inf")
            ctr = 0
            for f in frequencies:
                if c in f:
                    min_freq = min(min_freq, f[c])
                    ctr += 1

            if ctr == len(frequencies):
                res += c * min_freq

        return res