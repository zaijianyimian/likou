from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rightSum = [0] * n
        for i in range(n - 2, -1, -1):
            rightSum[i] = nums[i + 1] + rightSum[i + 1]
        leftSum = 0
        ans = []
        for i in range(n):
            ans.append(abs(rightSum[i] - leftSum))
            leftSum += nums[i]
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.leftRightDifference([10,4,8,3]))
