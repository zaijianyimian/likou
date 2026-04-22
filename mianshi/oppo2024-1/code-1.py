import sys
from typing import List

input = sys.stdin.readline


def getStatus(arr: List):
    INF = 10 ** 9 + 1
    min1, min2 = INF, INF
    max1, max2 = 0, 0
    for x in arr:
        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x
    return min1, min2, max1, max2


if __name__ == "__main__":
    n = int(input())
    power = []
    appearence = []
    sumA = 0
    sumB = 0
    for i in range(n):
        a, b = map(int, input().split())
        power.append(a)
        sumA += a
        appearence.append(b)
        sumB += b
    minpw1, minpw2, maxpw1, maxpw2 = getStatus(power)
    minap1, minap2, maxap1, maxap2 = getStatus(appearence)
    result = []
    for i in range(n):
        mipw = minpw2 if power[i] == minpw1 else minpw1
        mapw = maxpw2 if power[i] == maxpw1 else maxpw1
        miap = minap2 if appearence[i] == minap1 else minap1
        maap = maxap2 if appearence[i] == maxap1 else maxap1
        res = (sumA - mipw - mapw - power[i] + sumB - miap - maap - appearence[i]) / (n - 3) / 2
        result.append("%g" % res)
    print("\n".join(map(str, result)))

