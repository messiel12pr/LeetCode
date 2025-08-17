'''

    3477. Fruits Into Baskets II

'''

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits:
            for i in range(len(baskets)):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    break

        return len(baskets) - len(list(filter(lambda x: x == 0, baskets)))