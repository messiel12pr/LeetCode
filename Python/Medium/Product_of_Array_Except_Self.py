'''

    238. Product of Array Except Self

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0 for _ in range(n)]
        post = [0 for _ in range(n)]
        pre[0] = 1
        post[-1] = 1

        for i in range(n-1):
            pre[i + 1] = pre[i] * nums[i]

        for i in range(n-1, 0, -1):
            post[i - 1] = post[i] * nums[i]

        return [pre[i] * post[i] for i in range(n)]

