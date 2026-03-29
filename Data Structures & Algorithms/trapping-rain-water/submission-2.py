class Solution:
    def trap(self, height: List[int]) -> int:
        if (len(height) <= 2):
            return 0
        prefix = [0] * len(height)
        for i in range(1, len(height)):
            prefix[i] = max(height[i-1], prefix[i-1])
        
        suffix = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(height[i+1], suffix[i+1])
        
        res = 0
        for i in range(len(height)):
            res += max(0,min(prefix[i], suffix[i]) - height[i])

        return res
