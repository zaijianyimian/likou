class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lef = i + 1
            rig = len(nums) - 1
            while lef < rig:
                if nums[i] + nums[lef] + nums[rig] > 0:
                    rig -= 1
                elif nums[i] + nums[lef] + nums[rig] < 0:
                    lef += 1
                else:
                    res.append([nums[i], nums[lef], nums[rig]])
                    while lef < rig and nums[lef] == nums[lef + 1]:
                        lef += 1
                    while lef < rig and nums[rig] == nums[rig - 1]:
                        rig -= 1
                    lef += 1
                    rig -= 1
        return  res