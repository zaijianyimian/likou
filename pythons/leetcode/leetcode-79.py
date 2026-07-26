from typing import List

# 79 单词搜索
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(self, i: int, j: int, k: int) -> bool:
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = '#'
            res = backtrack(self, i + 1, j, k + 1) or backtrack(self, i - 1, j, k + 1) or backtrack(self, i, j + 1, k + 1) or backtrack(self, i, j - 1, k + 1)
            board[i][j] = word[k]
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(self, i, j, 0):
                    return True
        return False


