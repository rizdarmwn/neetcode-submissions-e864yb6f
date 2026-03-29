class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        highest_area = 0
        for i in range(len(heights)):
            h = heights[i]
            right = 0
            for j in range(i + 1, len(heights)):
                if h > heights[j]:
                    break
                right += 1
            left = 0
            for j in range(i - 1, -1, -1):
                if h > heights[j]:
                    break
                left += 1

            highest_area = max(h * (right + left + 1),highest_area)
            
        return highest_area


