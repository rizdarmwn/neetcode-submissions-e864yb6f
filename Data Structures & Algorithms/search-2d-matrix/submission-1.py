class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        t, b = 0, len(matrix) - 1

        while t <= b:
            row = (t + b) // 2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break
        
        if not (t <= b):
            return False
        
        row = (t + b) // 2
        l, r = 0, len(matrix[row]) - 1
        while l <=r:
            m = l + (r - l) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            elif target == matrix[row][m]:
                return True
        return False
                