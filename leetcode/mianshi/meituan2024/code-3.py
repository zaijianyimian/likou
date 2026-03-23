import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())
    st = input().strip()
    count = 0
    for i in st:
        if i == 'M' or i == 'T':
            count += 1
    print(min(len(st), count + k))
