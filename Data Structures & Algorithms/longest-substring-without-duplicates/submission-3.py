class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) <= 1):
            return len(s)
        chars = set()
        count = 0
        l, r = 0, 1
        chars.add(s[l])
        while r < len(s):
            if s[r] in chars:
                l += 1
                r = l + 1
                count = max(count, len(chars))
                chars.clear()
                chars.add(s[l])
            else:
                chars.add(s[r])
                r += 1
        
        return max(count, len(chars))
