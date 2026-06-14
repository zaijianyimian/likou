import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                tmp = board[r][c]
                if tmp == '.':
                    continue
# 唯一标识3*3矩阵
                    boxIndex = (r // 3) * 3 + c // 3
                if (tmp in row[r] or tmp in col[c] or tmp in boxes[boxIndex]):
                    return False
                row[r].add(tmp)
                col[c].add(tmp)
                boxes[boxIndex].add(tmp)
        return True