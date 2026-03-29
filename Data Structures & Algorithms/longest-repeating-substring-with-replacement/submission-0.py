class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, max_freq = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])
                window_size = j - i + 1
                if window_size - max_freq <= k:
                    res = max(res, window_size)
        
        return res

            
            
        

