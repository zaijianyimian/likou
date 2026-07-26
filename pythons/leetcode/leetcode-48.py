from typing import List
"""这道题要重新看"""
# 48. 旋转图像 看不懂
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) != len(matrix[0]):
            return
        n = len(matrix)
        # 先进行对角线反转
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]
        # 在进行上下反转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]