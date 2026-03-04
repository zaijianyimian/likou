from typing import List

# 238. 除自身以外数组的乘积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        flag = 0
        sum = 1
        for i in nums:
            if i == 0:
                flag += 1
            else:
                sum *= i
        if flag > 1:
            return [0]*len(nums)
        res = []
        for i in nums:
            if flag == 1 and i == 0:
                res.append(sum)
            elif flag == 1 and i != 0:
                res.append(0)
            elif flag == 0:
                res.append(sum//i)
        return res
