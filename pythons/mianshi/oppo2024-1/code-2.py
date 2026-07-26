import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()
    t = input().strip()
    target = input().strip()
    for i in range(len(s)):
        if s[i] == target[i] or t[i] == target[i]:
            continue
        else:
            print("No")
            return
    print("Yes")
if __name__=="__main__":
    solve()
