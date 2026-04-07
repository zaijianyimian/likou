import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        m = int(input())
        a = list(map(int,input().split()))
        print(len(set(a)))
