'''

    2570. Merge Two 2D Arrays by Summing Values 

    Kinda brute force solution

'''

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        itr1 = itr2 = sum = 0
        arr = []

        while itr1 != len(nums1) or itr2 != len(nums2):
            
            if itr1 == len(nums1):
                while itr2 != len(nums2):
                    arr.append((nums2[itr2][0], nums2[itr2][1]))
                    itr2 = itr2 + 1

            elif itr2 == len(nums2):
                while itr1 != len(nums1):
                    arr.append((nums1[itr1][0], nums1[itr1][1]))
                    itr1 = itr1 + 1

            else:
                if nums1[itr1][0] == nums2[itr2][0]:
                    sum = nums1[itr1][1] + nums2[itr2][1]
                    arr.append((nums1[itr1][0], sum))
                    itr1 = itr1 + 1
                    itr2 = itr2 + 1

                elif nums1[itr1][0] < nums2[itr2][0]:
                    arr.append((nums1[itr1][0], nums1[itr1][1]))
                    itr1 = itr1 + 1

                else:
                    arr.append((nums2[itr2][0], nums2[itr2][1]))
                    itr2 = itr2 + 1

        return arr