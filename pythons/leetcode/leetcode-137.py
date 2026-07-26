from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        """题目中整数一般按32位有符号整数处理，int，4字节
        所以枚举0~31这32个二进制位数
        """
        for i in range(32):
            cnt = 0 # 统计所有数字在第i位上一共有多少个1
            # 取出第i位的数据
            for num in nums:
                bit = (num >> i) & 1
                cnt += bit
            if cnt % 3 != 0:
                ans |= 1 << i
        # python中不按32位有符号整数处理
        if ans >= 2 ** 31:
            ans -= 2 ** 32
        return ans
