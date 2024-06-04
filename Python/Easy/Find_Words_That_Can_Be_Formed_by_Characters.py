'''

    1160. Find Words That Can Be Formed by Characters

'''

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch = [0] * 26
        for c in chars:
            ch[ord(c) - ord('a')] += 1
        
        res = 0
        for word in words:
            ch2 = [x for x in ch]
            for c in word:
                ch2[ord(c) - ord('a')] -= 1
                if ch2[ord(c) - ord('a')] == -1:
                    break

            if -1 not in ch2:
                res += len(word)

        return res