import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        lst = []
        for n in nums:
            if m.get(n, None) is not None:
                m[n] += 1
            else:
                m[n] = 1
        
        for key in m:
            heapq.heappush(lst, (m[key], key))
            if len(lst) > k:
                heapq.heappop(lst)

        res = []
        for i in range(k):
            res.append(heapq.heappop(lst)[1])

        return res
