import collections
from typing import List

# 994 腐烂的橘子 广度优先遍历
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        ans = 0
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        while queue and fresh > 0:
            ans += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx,ny = x+dx,y+dy
                    if nx < 0 or nx >= len(grid) or ny >= len(grid[0]) or ny < 0 or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    fresh -= 1
                    queue.append((nx,ny))
        return -1 if fresh > 0 else ans

