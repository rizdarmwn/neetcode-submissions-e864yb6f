class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct1, dct2 = {}, {}
        for c in s:
            if dct1.get(c):
                dct1[c] += 1
            else:
                dct1[c] = 1
        
        for c in t:
            if dct2.get(c):
                dct2[c] += 1
            else:
                dct2[c] = 1
        
        for k in dct1:
            if dct2.get(k) and dct2[k] != dct1[k]:
                return False
            elif dct2.get(k, None) is None:
                return False
        return len(dct1) == len(dct2) and True
                

                