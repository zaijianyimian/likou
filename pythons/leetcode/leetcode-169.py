from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums) // 2]

        host, hp = 0, 0
        for i in nums:
            if hp == 0:
                host = i
                hp += 1
            else:
                if i == host:
                    hp += 1
                else:
                    hp -= 1
        return host

s = Solution()
print(s.majorityElement([6,5,5]))