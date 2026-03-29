class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            print(s)
            try:
                i_t = int(t)
                s.append(i_t)
            except ValueError:
                match t:
                    case "+":
                        rs = s.pop()
                        ls = s.pop()
                        res = ls + rs
                        s.append(res)
                    case '-':
                        rs = s.pop()
                        ls = s.pop()
                        res = ls - rs
                        s.append(res)
                    case '*':
                        rs = s.pop()
                        ls = s.pop()
                        res = ls * rs
                        s.append(res)
                    case '/':
                        rs = s.pop()
                        ls = s.pop()
                        res = int(ls / rs)
                        s.append(res)
        
        return s[0]
                