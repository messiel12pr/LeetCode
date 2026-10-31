'''

    208. Implement Trie (Prefix Tree)

'''

class Trie:

    def __init__(self, c=''):
        self.caracter = c
        self.characters = [None] * 27
        self.end = False
        

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if not node.characters[ord(c) - ord('a')]:
                node.characters[ord(c) - ord('a')] = Trie(c)
            node = node.characters[ord(c) - ord('a')]
        node.end = True
        

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if not node.characters[ord(c) - ord('a')]:
                return False
            
            node = node.characters[ord(c) - ord('a')]

        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if not node.characters[ord(c) - ord('a')]:
                return False
            
            node = node.characters[ord(c) - ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
