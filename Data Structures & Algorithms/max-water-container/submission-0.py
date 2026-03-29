class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float("-inf")
        max_width = len(heights) - 1
        l, r = 0, len(heights) - 1

        while max_width > 0:
            length = r - l
            width = min(heights[l], heights[r])
            area = length * width
            if max_area < area:
                max_area = area
            if r == len(heights) - 1:
                max_width -= 1
                r = max_width 
                l = 0
            else:
                r += 1
                l += 1
            
        
        return max_area
            