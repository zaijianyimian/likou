import collections
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    MOD = 1000000007
    k,n = map(int,input().split())
    queue = collections.deque()
    dic = collections.defaultdict(int)
    arr = []
    max = 0
    for i in range(n):
        num = int(input())
        dic[num] = 0
        arr.append(num)
        if num > max:
            max = num
    l = r = 1
    su = 0
    while r <= k:
        queue.append(1)
        su += 1
        if r in dic:
            dic[r] = 1
        r += 1
    index = r
    while index <= max:
        num = su
        su -= queue.popleft()
        su += num
        queue.append(num)
        if index in dic:
            dic[index] = num
        index += 1
    for i in arr:
        print(dic[i] % MOD)
