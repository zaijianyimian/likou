from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hp,host = 0,0
        for num in nums:
            if hp == 0:
                host = num
                hp += 1
            elif num == host:
                hp += 1
            else:
                hp -= 1
        return host