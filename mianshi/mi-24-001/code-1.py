import collections
import sys
input = sys.stdin.readline

if __name__=="__main__":
    n,k,a,b = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    good = [1 if arr1[i] >= a and arr2[i] >= b else 0 for i in range(n)]
    good += good[:k - 1]

    cnt = sum(good[:k])
    ans = 1 if cnt == k else 0

    for i in range(k, n + k - 1):
        cnt += good[i]
        cnt -= good[i - k]
        if cnt == k:
            ans += 1

    print(ans)


