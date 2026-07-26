class Solution:
    def divide(self, a: int, b: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        if a == INT_MIN and b == -1:
            return INT_MAX
        flag = 0
        if a < 0:
            a = -a
            flag += 1
        if b < 0:
            b = -b
            flag += 1
        ans = 0
        while b <= a:
            tmp = b
            count = 1
            while a > tmp + tmp:
                tmp += tmp
                count += count
            ans += count
            a -= tmp
        return -ans if  flag == 1 else ans