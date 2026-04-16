import sys

import math

input= sys.stdin.readline

if __name__== "__main__":
    n,m  = map(int,input().split())
    arr = list(map(str,input().split()))
    st = list(input().strip())
    se = set(arr)
    pre = [-1] * n
    last = [-1] * n
    tmp = -1
    for i,x in enumerate(st):
        if x in se:
            tmp = i
            continue
        pre[i] = tmp
    tmp = -1
    for i in range(n - 1,-1,-1):
        if st[i] in se:
            tmp = i
        last[i] = tmp
    res = []
    for i in range(n):
        if st[i] in se:
            res.append(st[i])
            continue
        lInd = pre[i]
        rInd = last[i]
        if lInd != -1 and rInd != -1:
            distL = i - lInd
            distR = rInd - i
            if distL <= distR:
                res.append(st[lInd])
            else:
                res.append(st[rInd])
        elif lInd != -1:
            res.append(st[lInd])
        elif rInd != -1:
            res.append(st[rInd])
    print("".join(res))