'''

    1436. Destination City


'''

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        incoming = set([x for x, y in paths])
        outgoing = set([y for x, y in paths])
        return list(outgoing - incoming)[0]