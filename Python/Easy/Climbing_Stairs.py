'''

    70. Climbing Stairs

'''

class Solution:
    def __init__(self):
            self.steps = {1: 1, 2: 2}
            
    def climbStairs(self, n: int) -> int:
        if n in self.steps:
            return self.steps[n]

        self.steps[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.steps[n]
