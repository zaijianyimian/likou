from typing import List


# 54. 螺旋矩阵
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        while left <= right and top <= bottom:
            # 从左到右遍历上边界
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # 检查是否还有行需要处理
            if top > bottom:
                break

            # 从上到下遍历右边界
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # 检查是否还有列需要处理
            if left > right:
                break

            # 从右到左遍历下边界
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            # 检查是否还有行需要处理
            if top > bottom:
                break

            # 从下到上遍历左边界
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
