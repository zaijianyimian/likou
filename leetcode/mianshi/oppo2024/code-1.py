import sys
input = sys.stdin.readline

if __name__=="__main__":
    n,ws = map(int,input().split())
    ans = 0
    for i in range(n):
        a,b = map(int,input().split())
        if a <= ws:
            ans += b
            ws -= a
    print(ans)