from idlelib import window


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[0] == '1':
            return False
        f = [False] * n
        f[0] = True
        window = 0
        for i in range(1,n):
            if s[i] == '1':
                continue
            if i - minJump >= 0 and f[i - minJump]:
                window += 1
            if i - maxJump - 1 >= 0 and f[i - maxJump - 1]:
                window -= 1
            if s[i] == '0' and window > 0:
                f[i] = True
        return f[-1]
