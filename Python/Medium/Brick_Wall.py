class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        len_wall = sum(wall[0])
        hm = defaultdict(int)

        for i in range(len(wall)):
            temp = 0
            for brick in wall[i]:
                temp += brick
                hm[temp] += 1

        hm[len_wall] = 0

        return len(wall) - max(hm.values())  