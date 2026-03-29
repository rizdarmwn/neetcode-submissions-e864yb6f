class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) <= 1):
            return len(s)
        chars = set()
        count = 0
        l, r = 0, 1
        chars.add(s[l])
        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            count = max(count, r - l + 1)
            r += 1

        return count
