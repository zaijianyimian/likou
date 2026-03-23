import sys
input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    for i in range(n):
        s = input().strip()
        if  not (s and set(s).issubset({"P","A","T"})):
            print("NO")
            continue
        pInd = s.find("P")
        tInd = s.rfind("T")
        leftA = pInd
        midInd = tInd - pInd - 1
        rightA = len(s) - tInd - 1
        if s.count("P") != 1 or s.count("T") != 1:
            print("NO")
            continue
        if midInd >= 1 and midInd * leftA == rightA:
            print("YES")
        else:
            print("NO")