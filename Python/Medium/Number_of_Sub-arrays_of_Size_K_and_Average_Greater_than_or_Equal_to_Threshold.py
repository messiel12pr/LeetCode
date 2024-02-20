'''
    1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

    Solution:
'''

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r, res, curr_sum = 0, 0, 0, 0

        while r < len(arr):
            curr_sum += arr[r]

            if r - l == k - 1:
                if curr_sum//k >= threshold:
                    res += 1

                curr_sum -= arr[l]
                l += 1
            
            r += 1

        return res