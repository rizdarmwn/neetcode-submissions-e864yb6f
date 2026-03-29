class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in strs:
            lst = [0] * 26
            for c in s:
                lst[ord(c) - ord('a')] += 1
            tup = tuple(lst)
            if m.get(tup, None) is not None:
                m[tup].append(s)
            else:
                m[tup] = [s]
        
        res = []
        for k in m:
            res.append(m[k])
        
        return res