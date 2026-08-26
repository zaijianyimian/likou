import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
q = int(input())
for i in range(q):
    x = int(input())
    for w,a,b in arr:
        if x > w:
            x = x - b if x - b > 0 else 0
        else:
            x += a
    print(x)

