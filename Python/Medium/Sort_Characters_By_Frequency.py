'''

    451. Sort Characters By Frequency

    Solution

'''

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = 63 * [('', 0)]
        res = ''

        for i in s:
            if i.isdigit():
                freq[int(i)] = (i, freq[int(i)][1] + 1)

            elif i.isupper():
                freq[ord(i) - ord('A') + 37] = (i, freq[ord(i) - ord('A') + 37][1] + 1)

            else:
                freq[ord(i) - ord('a') + 10] = (i, freq[ord(i) - ord('a') + 10][1] + 1)

        freq = sorted(freq, key=lambda x: x[1], reverse=True)

        for i in freq:
            res += str(i[0] * i[1])

        return res