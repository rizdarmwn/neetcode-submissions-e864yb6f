class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}

        for v in s:
            if v in d1:
                d1[v] += 1
            else:
                d1[v] = 1
        
        for v in t:
            if v in d2:
                d2[v] += 1
            else:
                d2[v] = 1
        
        for k in d1:
            if d2.get(k) == None or d2.get(k) != d1.get(k):
                return False
        
        return True
