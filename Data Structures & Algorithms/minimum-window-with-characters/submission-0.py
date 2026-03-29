class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(t) > len(s)):
            return ""
        t_hm = {}
        for i in range(len(t)):
            t_hm[t[i]] = t_hm.get(t[i], 0) + 1

        l = 0
        s_hm = {}
        have = 0
        need = len(t_hm)
        res = [-1, -1]
        resLen = float('inf')
        for r in range(len(s)):
            s_hm[s[r]] = s_hm.get(s[r], 0) + 1
            if (s[r] in t_hm and s_hm[s[r]] == t_hm[s[r]]):
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                s_hm[s[l]] -= 1
                if (s[l] in t_hm and s_hm[s[l]] < t_hm[s[l]]):
                    have -= 1
                l += 1
        l, r = res[0], res[1] 
        
        return s[l: r+1] if resLen != float('inf') else ""


