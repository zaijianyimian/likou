from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 10 ** 6
        left = right = 0
        tmp = 0
        while right < len(nums):
            while right < len(nums) and tmp < target:
                tmp += nums[right]
                right += 1
            while left <= right and tmp >= target:
                if tmp >= target:
                    ans = min(ans, right - left) # 收缩窗口时再统计，如果在增加窗口后统计会出现窗口比实际的大的情况
                tmp -= nums[left]
                left += 1
        return ans if ans != 10 ** 6 else 0
if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(4, [1,4,4]))