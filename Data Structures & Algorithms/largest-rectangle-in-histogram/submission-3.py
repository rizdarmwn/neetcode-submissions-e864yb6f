class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        highest_area = 0

        stack = []
        leftMost = [-1] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        
        stack = []
        rightMost = [len(heights)] * len(heights)
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        for i in range(len(heights)):
            rightMost[i] -= 1
            leftMost[i] += 1
            highest_area = max(highest_area, (heights[i] * (rightMost[i] - leftMost[i] + 1)))
            
        return highest_area


