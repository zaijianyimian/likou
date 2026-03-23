import sys
input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    ans = []
    tmp = set()
    for i in a:
        while i > 1:
            if i %2 == 0:
                i = i // 2
            else:
                i = (i * 3 + 1) //2
            tmp.add(i)
    for i in a:
        if i not in tmp:
            ans.append(i)
    ans.sort(reverse=True)
    print(*ans)
