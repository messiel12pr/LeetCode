'''

    912. Sort an Array

'''


class Solution:
    def merge(self, half_1, half_2):
        merged = []
    
        while half_1 or half_2:
            if half_1 and half_2:
                if half_1[0] <= half_2[0]:
                    merged.append(half_1.pop(0))

                else:
                    merged.append(half_2.pop(0))

            if half_1 and not half_2:
                while half_1:
                    merged.append(half_1.pop(0))

            elif half_2 and not half_1:
                while half_2:
                    merged.append(half_2.pop(0))

        return merged

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:

            half_1 = nums[:len(nums)//2]
            half_2 = nums[len(nums)//2:]

            half_1 = self.sortArray(half_1)
            half_2 = self.sortArray(half_2)

            return self.merge(half_1, half_2)

        return nums
