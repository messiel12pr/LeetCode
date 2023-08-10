'''

    3. Longest Substring Without Repeating Characters

    Solution

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_str = ""
        longest = 0
        for i in range(len(s)):
            if s[i] in temp_str:
                while s[i] in temp_str:
                    temp_str = temp_str.replace(temp_str[0], "", 1)

            temp_str += s[i]
                
            if len(temp_str) > longest:
                longest = len(temp_str)
        return longest
