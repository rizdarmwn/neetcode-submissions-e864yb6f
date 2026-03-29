class Solution:
    @staticmethod
    def ceil(a: int, b: int):
        return -(a // -b)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = 0
        for i in range(len(piles)):
            max_val = max(piles[i], max_val)
        
        l, r = 1, max_val
        res = 0
        while l <= r:
            m = l + (r - l) // 2

            total = 0
            for i in range(len(piles)):
                total += Solution.ceil(piles[i], m)
            
            if total <= h:
                res = m
                r = m - 1
            elif total > h:
                l = m + 1
        
        return res

