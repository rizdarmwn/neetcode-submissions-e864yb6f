class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        hm = {}
        max_f = 0
        l, r = 0, 0
        while r < len(s):
            hm[s[r]] = hm.get(s[r], 0) + 1
            max_f = max(hm[s[r]], max_f)
            while (r - l + 1) - max_f > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        
        return res