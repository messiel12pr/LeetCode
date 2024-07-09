'''

    659. Encode and Decode Strings

'''

class Solution:
    idxs = []
    def encode(self, strs: List[str]) -> str:
        self.idxs = []
        length = 0
        for i in strs:
            length += len(i)
            self.idxs.append(length)
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        decoded = []
        length = 0
        for i in self.idxs:
            decoded.append(s[length:i])
            length = i
        return decoded