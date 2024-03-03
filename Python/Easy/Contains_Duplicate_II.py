'''
    219. Contains Duplicate II

    Solution:
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        visited = set()

        for r in range(len(nums)):
            if r - l > k:
                visited.remove(nums[l])
                l += 1

            if nums[r] in visited:
                return True

            visited.add(nums[r])
        
        return False