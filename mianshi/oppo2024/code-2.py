import sys

input = sys.stdin.readline

if __name__ == "__main__":
    st = input().strip()
    k = int(input().strip())
    n = len(st)
    if k > n:
        print('a' * (k - n) + st[::-1])
    elif k == len(st):
        print(st[::-1])
    else:
        if st[k:] == st[k:][::-1]:
            print(st[:k][::-1])
        elif st[0:n - k] == st[:n - k][::-1]:
            print(st[n - k:][::-1])
        else:
            print(-1)
