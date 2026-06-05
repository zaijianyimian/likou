from functools import lru_cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        melidroni = (num1,num2)
        def calc(n: int) -> int:
            if n <= 100:
                return 0
            s = str(n)
            m = len(s)
            @lru_cache(None)
            def dfs(pos: int,pre2 : int,pre1:int,started:bool,tight:bool) :
                if pos == m:
                    return 1,0
                up = int(s[pos]) if tight else 9
                totalCnt = 0
                totalWav = 0
                for x in range(up + 1):
                    ntight = tight and x == up
                    if not started and x == 0:
                        cnt,wav = dfs(pos + 1,-1,-1,False,ntight)
                        totalCnt += cnt
                        totalWav += wav
                        continue
                    if not started:
                        cnt,wav = dfs(pos + 1,-1,x,True,ntight)
                        totalCnt += cnt
                        totalWav += wav
                        continue
                    add = 0
                    if pre2 != -1:
                        if pre1 > pre2 and pre1 > x:
                            add = 1
                        elif pre1 < pre2 and pre1 < x:
                            add = 1
                    cnt, wav = dfs(pos + 1, pre1, x, True, ntight)
                    totalCnt += cnt
                    totalWav += wav +add * cnt
                return totalCnt,totalWav
            return dfs(0,-1,-1,False,True)[1]
        return calc(num2) - calc(num1 - 1)