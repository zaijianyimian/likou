from typing import List

# 739 每日温度
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        stack = [0]
        for i in range(1,len(temperatures)):
            if temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    arr[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return arr