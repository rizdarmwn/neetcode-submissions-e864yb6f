class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rule 1
        nums = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and board[i][j] in nums:
                    return False
                nums.add(board[i][j])
            nums.clear()
        
        # Rule 2
        for i in range(9):
            for j in range(9):
                if board[j][i] != "." and board[j][i] in nums:
                    return False
                nums.add(board[j][i])
            nums.clear()
        
        # Rule 3
        for square in range(9):
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] != "." and board[row][col] in nums:
                        return False
                    nums.add(board[row][col])
            nums.clear()
        
        return True