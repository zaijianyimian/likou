import sys
input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    max = 0
    min = 100
    maxList = []
    minList = []
    for i in range(n):
        arr = input().split()
        if int(arr[2]) > max:
            max = int(arr[2])
            maxList = [arr[0], arr[1]]
        if int(arr[2]) < min:
            min = int(arr[2])
            minList = [arr[0], arr[1]]
    print(" ".join(maxList))
    print(" ".join(minList))