class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 

        while (l < r):
            left_char = s[l].lower()
            right_char = s[r].lower()
            if not left_char.isalnum():
                l += 1
                continue
            if not right_char.isalnum():
                r -= 1
                continue
            if left_char != right_char:
                return False
            l += 1
            r -= 1

        
        return True