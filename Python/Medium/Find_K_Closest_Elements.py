'''
    658. Find K Closest Elements

    Solution:
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while l < r:
            if r - l + 1 == k:
                return arr[l:r+1]

            if abs(arr[r] - x) < abs(arr[l] - x):
                l += 1
            
            else:
                r -= 1

        return [arr[l]]