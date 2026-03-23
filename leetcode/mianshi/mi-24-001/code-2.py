import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    flag = False
    for i in range(m):
        queries.append(list(map(int, input().split())))
    for i in range(m):
        l = queries[i][0]
        r = queries[i][1]
        h = queries[i][2]
        for j in range(max(0,l - 1),min(n,r)):
            arr[j] -= h
            if arr[j] <= 0:
                print(i + 1)
                flag = True
                break
        if flag:
            break
