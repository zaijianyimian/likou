from typing import List

# 51. N皇后
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [['.']*n for _ in range(n)]
        res = []
        self.backtrack(0,n,res)
        return res
    def isValid(self,row,col,n):
        for i in range(row): # 判断同一列
            if self.board[i][col] == 'Q':
                return False
        i,j = row-1,col-1
        while i >= 0 and j >= 0: # 判断左上
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i,j = row - 1,col + 1
        while i >= 0 and j < n: # 判断右上
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return  True
    def backtrack(self,row,n,res):
        if row == n:
            solution = [''.join(row) for row in self.board]
            res.append(solution)
            return
        for col in range(n):
            if not self.isValid(row,col,n):
                continue
            self.board[row][col] = 'Q'
            self.backtrack(row+1,n,res)
            self.board[row][col] = '.'
