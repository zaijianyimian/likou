from typing import List


class Solution:
    def __init__(self):
        self.count = 0
        self.dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j)
                    self.count += 1
        return self.count
    def dfs(self,grid: List[List[str]],i: int,j: int):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "0"
        for dir in self.dirs:
            self.dfs(grid,i+dir[0],j+dir[1])


