from ast import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ans = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        if i < m:
            ans.extend(nums1[i:m])
        else:
            ans.extend(nums2[j:n])
        nums1[:] =  ans