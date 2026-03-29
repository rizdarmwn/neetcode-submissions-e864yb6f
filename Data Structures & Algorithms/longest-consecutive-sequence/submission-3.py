class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        longest = 0

        for n in hs:
            length = 1
            while (n + length) in hs:
                length += 1
            longest = max(length, longest)
        
        return longest
