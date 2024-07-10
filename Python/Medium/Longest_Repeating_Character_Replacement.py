'''

    424. Longest Repeating Character Replacement

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, l = 0, 0
        cnt = {}

        for idx, num in enumerate(s):
            cnt[num] = cnt.get(num, 0) + 1
            
            max_letter = max(cnt.values())
            window_len = idx - l + 1
            
            while window_len - max_letter > k:
                cnt[s[l]] -= 1
                window_len -= 1
                max_letter = max(cnt.values())
                l += 1
            
            res = max(res, window_len)

        return res