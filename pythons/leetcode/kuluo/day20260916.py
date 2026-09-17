import sys
import time

n, p = sys.stdin.readline().split()
start_time = time.time()
p = int(p)

m = len(n)
path = [''] * m


def dfs(i:int):
    if i == m:
        num = ''.join(path)

        if int(num) % p == 0:
            return num
        return None
    d = int(n[i])
    for x in (d - 1,d,d + 1):
        if 0 <= x <= 9:
            path[i] = str(x)
            ans = dfs(i + 1)
            if ans is not None:
                return ans
    return None

ans = dfs(0)
if ans is None:
    print(-1)
else:
    print(ans)
end_time = time.time()
print(end_time - start_time)
