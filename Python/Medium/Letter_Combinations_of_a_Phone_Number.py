'''

    17. Letter Combinations of a Phone Number

'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 
              6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        res = []
        if not digits:
            return []

        def backtrack(n, current):
            if n == len(digits):
                res.append(''.join(current))

            else:
                for j in hm[int(digits[n])]:
                    current.append(j)
                    backtrack(n+1, current)
                    current.pop()

        backtrack(0, [])
        return res