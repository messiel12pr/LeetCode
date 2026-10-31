'''

    1679. Max Number of K-Sum Pairs

'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''

            scan array and count frequency of elements
            itr array and for each index, calculate k - index
            check if that difference is in the hm
            if so check if k - index are equal
            if so check if hm[k-index] > 1
            update our counter accordingly
        
        '''

        hm = {}
        count = 0

        for i in nums:
            if i in hm:
                hm[i] += 1

            else:
                hm[i] = 1

        for i in range(len(nums)):
            diff = k - nums[i]

            if diff in hm and diff != nums[i] and hm[diff] > 0 and hm[nums[i]] > 0:
                hm[nums[i]] -= 1
                hm[diff] -= 1
                count += 1

            elif diff in hm and diff == nums[i] and hm[diff] > 1:
                hm[nums[i]] -= 1
                hm[diff] -= 1
                count += 1

        return count
