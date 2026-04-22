import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    su = sum(arr)
    tmp = arr[0]
    su -= tmp
    ans = tmp * su
    for i in range(1,n - 1):
        tmp += arr[i]
        su -= arr[i]
        ans = min(ans, tmp * su)
    print(ans)
