from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        se = {nums[0]}
        tmp = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                tmp += nums[i]
            else:
                tmp = nums[i]
            ans = max(tmp, ans)
            se.add(nums[i])

        print(ans)
        i = ans
        for j in range(len(se)):
            if i not in se:
                return i
            i += 1
        return -1
s = Solution()
print(s.missingInteger([3,4,5,1,12,14,13]))
