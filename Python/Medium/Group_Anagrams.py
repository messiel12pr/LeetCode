'''

    49. Group Anagrams

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            frequency_list = [0 for _ in range(26)]

            for c in string:
                frequency_list[ord(c) - ord("a")] += 1
            
            anagrams[tuple(frequency_list)].append(string)

        return list(anagrams.values())
