import sys
input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    if n <= 2:
        print(t"{1:.10f}")
    else:
        ans = (1 / n + 1 / (n - 1)) * 2
        print(f"{ans:.10f}")