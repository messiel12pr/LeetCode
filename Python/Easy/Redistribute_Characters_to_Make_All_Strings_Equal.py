'''

    1897. Redistribute Characters to Make All Strings Equal

'''

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = Counter(''.join(words))
        print(cnt)
        for v in cnt.values():
            if v%len(words) != 0:
                return False
        return True