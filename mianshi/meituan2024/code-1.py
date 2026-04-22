import sys
input = sys.stdin.readline
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    s = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n):
        rowstr = arr[i]
        for j in range(n):
            s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + (1 if rowstr[j] == '1' else -1)
    for k in range(1,n + 1):
        if k % 2 == 1:
            print(0)
            continue
        count = 0
        for i in range(k,n + 1):
            for j in range(k,n + 1):
                #这里为什么要这样算？，保存
                curSum = s[i][j] - s[i - k][j] - s[i][j - k] + s[i - k][j - k]
                if curSum == 0:
                    count += 1
        print(count)





