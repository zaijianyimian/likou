import sys
input = sys.stdin.readline

if __name__ == '__main__':
    MOD = 1000000007
    k,n = map(int,input().split())
    max = 0
    arr = []
    for i in range(n):
        num = int(input())
        arr.append(num)
        if num > max:
            max = num
    dp = [1] * (max + 1)
    l = r = 0
    sum = 0
    while r < k:
        sum += dp[r]
        r += 1
    start = r
    for i in range(start,max + 1):
        dp[i] = sum
        sum -= dp[l]
        l += 1
        sum += dp[r]
        r += 1
    for i in arr:
        # print(f'{i} ({dp[i - 1] % MOD})')
        print(dp[i - 1] % MOD)