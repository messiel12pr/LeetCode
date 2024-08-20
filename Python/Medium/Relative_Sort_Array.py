'''

    1122. Relative Sort Array

'''

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        end = sorted(list(set(arr1).difference(arr2)))
        arr2.extend(end)
        cnt = Counter(arr1)
        res = []

        for n in arr2:
            for _ in range(cnt[n]):
                res.append(n)

        return res