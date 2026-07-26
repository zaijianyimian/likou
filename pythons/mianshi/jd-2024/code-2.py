import collections
import sys
input = sys.stdin.readline
dic = collections.defaultdict()

if __name__=="__main__":
    arr = list(input().strip())
    dic = {char: i for i,char in enumerate(arr)}
    n = int(input().strip())
    ansTmp = []
    for i in range(n):
        ansTmp.append(input().strip())
    ansTmp.sort(key=lambda x: [dic[char] for char in x])
    print("\n".join(ansTmp))
