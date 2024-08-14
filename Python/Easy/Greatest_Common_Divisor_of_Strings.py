'''

    1071. Greatest Common Divisor of Strings

'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        r = len(str1)
        
        while r > 0:
            if len(str1) % len(str1[0:r]) == 0 and len(str2) % len(str1[0:r]) == 0:
                len_1 = (len(str1) // len(str1[0:r]))
                len_2 = (len(str2) // len(str1[0:r]))
                
                if (str1[0:r] * len_1) == str1 and (str1[0:r] * len_2) == str2:
                    return str1[0:r]

            r -= 1 

        return ""