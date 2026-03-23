import sys
input = sys.stdin.readline

if __name__== "__main__":
    dic = {0:"ling",1:"yi",2:"er",3:"san",4:"si",5:"wu",6:"liu",7:"qi",8:"ba",9:"jiu"}
    numStr = input().strip()
    arr = [int(i) for i in numStr]
    num = sum(arr)
    num = str(num)
    ans = []
    for i in num:
        ans.append(dic[int(i)])
    print(" ".join(ans))
