'''

    973. K Closest Points to Origin

'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = defaultdict(list)

        for x, y in points:
            distances[sqrt(x**2 + y**2)].append((x, y))

        items = sorted(distances.items())
        res = []
        i = 0
        while i < k:
            for n in items[i][1]:
                res.append(n)
                i += 1

        return res