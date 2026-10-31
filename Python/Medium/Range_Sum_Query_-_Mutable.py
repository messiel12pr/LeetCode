'''

    307. Range Sum Query - Mutable

'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        self.arr = nums
        
        for i in range(self.n):
            self.update_init(i, nums[i])

    def update_init(self, index: int, val: int) -> None:
        self.arr[index] = val
        index += 1
        while index <= self.n:
            self.tree[index] += val
            index += index & (-index)
        
    def update(self, index: int, val: int) -> None:
        delta = val - self.arr[index]
        self.arr[index] = val
        index += 1
        while index <= self.n:
            self.tree[index] += delta
            index += index & (-index)

    def query(self, i):
        res = 0
        i += 1
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)
        return res
    
    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
