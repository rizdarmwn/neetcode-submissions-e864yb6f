class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i]) - 1

            if target > matrix[i][r]:
                continue

            while l <= r:
                m = l + (r - l) // 2
                if target == matrix[i][m]:
                    return True
                elif target > matrix[i][m]:
                    l = m + 1
                elif target < matrix[i][m]:
                    r = m - 1
        

        return False
                