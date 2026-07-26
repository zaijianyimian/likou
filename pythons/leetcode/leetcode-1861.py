from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        ans = [['.'] * m for _ in range(n)]

        for i in range(m):
            write_pos = n - 1  # 当前槽位可放置石头的最右位置
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    ans[j][m - 1 - i] = '*'
                    write_pos = j - 1  # 障碍物左侧开启新槽位
                elif boxGrid[i][j] == '#':
                    ans[write_pos][m - 1 - i] = '#'
                    write_pos -= 1
        return ans
