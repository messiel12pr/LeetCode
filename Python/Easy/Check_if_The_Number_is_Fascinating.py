'''

    2729. Check if The Number is Fascinating

'''

class Solution:
    def isFascinating(self, n: int) -> bool:
        res = []
        res.extend([x for x in str(n)])
        res.extend([x for x in str(2*n)])
        res.extend([x for x in str(3*n)])
        print(res)
        if sorted(res) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True
        return False
         
