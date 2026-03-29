class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        couple = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        st = []

        for c in s:
            if c in couple:
                st.append(c)
            else:
                if len(st) > 0:
                    c2 = st.pop()
                    if couple[c2] != c:
                        return False
                else:
                    return False
        
        return True if len(st) == 0 else False