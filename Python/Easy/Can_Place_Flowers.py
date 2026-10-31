'''

    605. Can Place Flowers

'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted_count = 0
        consecutive_count = 0
        flowerbed.insert(0,0)
        flowerbed.append(0)
        print(flowerbed)

        for i in flowerbed:
            if i == 0:
                consecutive_count += 1
            else:
                consecutive_count = 0
            
            if consecutive_count == 3:
                planted_count += 1
                consecutive_count = 1
        
            if planted_count == n:
                return True
        
        return False            
