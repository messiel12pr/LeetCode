'''

    567. Permutation in String


    Solution

'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_1 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 
                  'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0,    
                  'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 
                  's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 
                  'y':0, 'z':0}

        dict_2 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 
                  'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0,    
                  'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 
                  's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 
                  'y':0, 'z':0}
        l = 0
        r = 0

        for i in s1:
            dict_1[i] += 1

        while r < len(s2):
            if dict_1[s2[r]] > 0 and dict_2[s2[r]] < dict_1[s2[r]]:
                dict_2[s2[r]] += 1
                r += 1
            
            else:
                dict_2 =  dict.fromkeys(dict_2, 0)
                l += 1
                r = l 
            
            if dict_1 == dict_2:
                return True

        return False
