from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        row = self.searchRow(target,matrix)
        return self.searchCol(target,matrix,row)
    def searchRow(self,target,matrix) -> int:
        lef,rig = 0,len(matrix)-1
        while lef <= rig:
            mid = (lef+rig) // 2
            if matrix[mid][0] == target:
                return mid
            if matrix[mid][0] < target:
                lef = mid + 1 # 第一个大于等于target的元素
            else:
                rig = mid - 1# 最后一个小于target的位置
        return rig
    def searchCol(self,target,matrix,row) -> bool:
        lef,rig = 0,len(matrix[0])-1
        while lef <= rig:
            mid = (lef+rig) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                lef = mid + 1
            else:
                rig = mid - 1
        return False
