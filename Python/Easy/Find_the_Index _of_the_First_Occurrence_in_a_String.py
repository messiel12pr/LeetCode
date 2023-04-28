'''

    28. Find the Index of the First Occurrence in a String

    Kinda cheating by using regex but oh well ¯\_(ツ)_/¯

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = re.search(f'{needle}', haystack)

        if match:
            return match.start(0)
        return -1