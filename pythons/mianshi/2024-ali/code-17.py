import sys


def solve():
    # 快速读取所有输入数据
    # data[0] 是 n, data[1] 是字符串 s
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    s = data[1]

    # 1. 计算整个字符串数位之和对 3 取模的结果
    # 一个数能被 3 整除，当且仅当所有数位之和能被 3 整除
    total_sum_mod = 0
    digits = []
    for char in s:
        d = int(char)
        digits.append(d)
        total_sum_mod = (total_sum_mod + d) % 3

    # 2. 使用前缀和思想统计
    # 我们要删除一个区间 [l, r]，其数位和为 T
    # 剩余部分要能被 3 整除，意味着：(total_sum - T) % 3 == 0
    # 即：T % 3 == total_sum % 3

    # cnt[i] 记录到目前为止，前缀和模 3 为 i 的出现次数
    cnt = [0] * 3
    cnt[0] = 1  # 初始前缀和 P[0] = 0

    ans = 0
    curr_prefix_sum = 0

    # 遍历每一位数字，计算当前前缀和并寻找匹配的先前前缀和
    for x in digits:
        curr_prefix_sum = (curr_prefix_sum + x) % 3

        # 子区间 [l, r] 的和对 3 取模的结果为 (P[r] - P[l-1]) % 3
        # 我们需要找到满足 (curr_prefix_sum - prev_prefix_sum) % 3 == total_sum_mod 的 prev
        # 变形得：prev_prefix_sum = (curr_prefix_sum - total_sum_mod + 3) % 3
        target = (curr_prefix_sum - total_sum_mod + 3) % 3

        # 累加之前出现过多少次符合条件的前缀和，即代表有多少个合法的删除区间以当前位置结尾
        ans += cnt[target]

        # 将当前前缀和的余数存入计数器
        cnt[curr_prefix_sum] += 1

    # 3. 处理“不进行操作”的情况
    # 如果原字符串总和本身就是 3 的倍数，方案数加 1
    if total_sum_mod == 0:
        ans += 1

    print(ans)


if __name__ == "__main__":
    solve()