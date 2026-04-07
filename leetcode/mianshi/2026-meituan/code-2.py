import sys

input = sys.stdin.readline


def solve():
    n = input
    s = input()
    left_positon = [i + 1 for i, char in enumerate(s) if char == '(']
    ans = 0
    for k in range(len(left_positon)):
        limit = 2 * (k + 1) - 1
        if left_positon[k] > limit:
            ans += left_positon[k] - limit
    print(ans)


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m = int(input())
        solve()
