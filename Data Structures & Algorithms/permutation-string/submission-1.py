class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        MAX_ORD = 122
        s1_count = [0] * 26
        for i in range(len(s1)):
            s1_count[MAX_ORD - ord(s1[i])] += 1
        
        l = 0
        s2_count = [0] * 26
        for r in range(len(s2)):
            s2_count[MAX_ORD - ord(s2[r])] += 1

            if r - l + 1 > len(s1):
                s2_count[MAX_ORD - ord(s2[l])] -= 1
                l += 1
            
            if s1_count == s2_count:
                return True
        
        return False