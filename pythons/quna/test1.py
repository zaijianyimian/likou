import sys
input = sys.stdin.readline

n = int(input())
areas = []
for i in range(n):
    a,b = map(int,input().split())
    areas.append([a,b])
max_end = max(end for _,end in areas)
diff = [0] * (max_end + 2) # 加2防止次区间超出范围
for start,end in areas:
    diff[start] += 1
    diff[end + 1] -= 1
# 枚举区间
cover = 0
total_odd = 0
# 以当前位置结尾的最佳删除收益
current_gain = 0
best_gain = 0
for i in range(max_end + 1):
    cover += diff[i]
    if cover == 0:
        current_gain = 0
        continue
    if cover & 1:
        gain = -1
        total_odd += 1
    else:
        gain = 1
    current_gain = max(0,current_gain + gain)
    best_gain = max(best_gain,current_gain)
ans = total_odd + best_gain
print(ans)


