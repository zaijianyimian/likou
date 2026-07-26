import sys
import heapq
input = sys.stdin.readline

if __name__=="__main__":
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    totaltime = sum(arr)
    maxHeap = []
    itemCount = n // k
    curRight = n - 1
    for i in range(itemCount,0,-1):
        earnInd = i * k - 1
        while curRight > earnInd:
            heapq.heappush(maxHeap,-arr[curRight])
            curRight -= 1
        if maxHeap:
            totaltime += heapq.heappop(maxHeap)
    print(totaltime)
