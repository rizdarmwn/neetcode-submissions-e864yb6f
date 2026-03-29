import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        
        heap = []
        
        for n in nums:
            heapq.heappush(heap, n)
        
        longest = 1
        temp_longest = longest
        
        while (len(heap) > 0):
            lowest = heapq.heappop(heap)
            print(lowest)
            if (len(heap) == 0):
                break
            if (lowest == heap[0]):
                continue
            if (lowest + 1 == heap[0]):
                temp_longest += 1
            else:
                longest = max(longest, temp_longest)
                temp_longest = 1
        longest = max(longest, temp_longest)
        return longest