'''

    680. Valid Palindrome II

'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome_left() -> bool:
            ptr_l, ptr_r = 0, len(s) - 1
            flag = False

            while ptr_l < ptr_r:
                if s[ptr_l] != s[ptr_r] and not flag:
                    ptr_l += 1
                    flag = True

                elif s[ptr_l] != s[ptr_r] and flag:
                    return False

                else:
                    ptr_l += 1
                    ptr_r -= 1
            
            return True

        def check_palindrome_right() -> bool:
            ptr_l, ptr_r = 0, len(s) - 1
            flag = False

            while ptr_l < ptr_r:
                if s[ptr_l] != s[ptr_r] and not flag:
                    ptr_r -= 1
                    flag = True

                elif s[ptr_l] != s[ptr_r] and flag:
                    return False

                else:
                    ptr_l += 1
                    ptr_r -= 1

            return True

        return check_palindrome_left() or check_palindrome_right()
