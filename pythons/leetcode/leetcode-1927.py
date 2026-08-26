class Solution:
    def sumGame(self, num: str) -> bool:
        m = len(num) //2
        d = 0
        for i,x in enumerate(num):
            x = int(x) if x != '?' else 9
            d += x if i < m else -x
        return d == 0
