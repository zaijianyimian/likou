import collections
import sys
input = sys.stdin.readline

def compare(arr:list,arr2:list) -> bool:
    if arr[1] > arr2[1]:
        return True
    elif arr[1] < arr2[1]:
        return False
    else:
        if arr[2] > arr2[2]:
            return True
        elif arr[2] < arr2[2]:
            return False
        else:
            if arr[3] < arr2[3]:
                return True
            elif arr[3] > arr2[3]:
                return False
            else:
                return arr[0] < arr2[0]

if __name__ == "__main__":
    n, q = map(int, input().strip().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split())))
    dic = dict()
    queries = []
    for j in range(q):
        queries.append(list(map(int, input().strip().split())))
    for i in range(n):
        emp = arr[i][0]
        if arr[i][0] in dic.keys():
            ans = compare(dic[emp], arr[i])
            if not ans:
                dic[emp] = arr[i]
        else:
            dic[emp] = arr[i]
        dic[emp].append(i + 1)
    dic1 = dict()
    anssort = []
    arr.clear()
    for i in dic.keys():
        emp = dic[i][4]
        dic1[emp] = dic[i]
        anssort.append(dic[i])
    dic.clear()
    anssort.sort(key=lambda x: (-x[1], -x[2], x[3]),reverse=True)
    # print(anssort)
    for i in range(len(anssort)):
        emp = anssort[i][4]
        dic1[emp].append(i + 1)
    for i in queries:
        if i[0] not in dic1.keys():
            print(0)
        else:
            print(dic1[i[0]][-1])





