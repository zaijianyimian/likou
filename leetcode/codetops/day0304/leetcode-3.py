class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr =  [0] * 256
        left = right = 0
        res = 0
        while right < len(s):
            arr[ord(s[right])] += 1
            right += 1
            while arr[ord(s[right-1])] > 1:
                arr[ord(s[left])] -= 1
                left += 1
            res = max(res, right - left)
        return res