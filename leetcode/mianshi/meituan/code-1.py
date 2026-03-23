import sys

for line in sys.stdin:
    a = line.split()
    l = int(a[0])
    r = int(a[1])
    ans = 0
    for i in range(l, r + 1):
        count = 1
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count % 2 == 1:
            ans += 1
    print(ans)