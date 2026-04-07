from typing import List


# 超时 只在周长上运行，可以考虑周长取模法
# class Robot:
#
#     def __init__(self, width: int, height: int):
#         self.x = 0
#         self.y = 0
#         self.width = width
#         self.height = height
#         self.arr = [[0] * width for _ in range(height)]
#         self.directions = [(1,0),(0,1),(-1,0),(0,-1)]
#         self.dir = 0
#
#     def step(self, num: int) -> None:
#         if num > 0:
#             for i in range(num):
#                 if self.x + self.directions[self.dir][0] < self.width and self.y +self.directions[self.dir][1] < self.height and self.x + self.directions[self.dir][0] >= 0 and self.y + self.directions[self.dir][1] >= 0 and self.arr[self.y + self.directions[self.dir][1]][self.x + self.directions[self.dir][0]] == 0:
#                     self.x += self.directions[self.dir][0]
#                     self.y += self.directions[self.dir][1]
#                 else:
#                     self.dir = (self.dir + 1) % 4
#                     self.x += self.directions[self.dir][0]
#                     self.y += self.directions[self.dir][1]
#
#     def getPos(self) -> List[int]:
#         return [self.x, self.y]
#
#     def getDir(self) -> str:
#         ans =  ["East","North","West","South"]
#         return ans[self.dir]
class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.moved = 0  # 标记是否移动过，用于判断（0，0）点的方向
        self.peri = (self.w + self.h - 2) * 2

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.peri

    def getPos(self) -> List[int]:
        p = self.pos
        w, h = self.w, self.h
        if p < w:
            return [p, 0]
            # 2. 右边
        if p < w + h - 1:
            return [w - 1, p - (w - 1)]
            # 3. 顶边
        if p < 2 * w + h - 2:
            return [w - 1 - (p - (w + h - 2)), h - 1]
            # 4. 左边
        return [0, h - 1 - (p - (2 * w + h - 3))]

    def getDir(self) -> str:
        p = self.pos
        w, h = self.w, self.h
        if self.moved and p == 0:
            return "South"
        if 1 <= p <= w - 1:
            return "East"
        elif w <= p <= w + h - 2:
            return "North"
        elif w + h - 2 <= p <= 2 * w + h - 3:
            return "West"
        return "South" if self.moved else "East"
