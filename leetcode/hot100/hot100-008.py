class Solution:
    # leetcode-3
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [0] * 256
        left = right = 0
        res = 0
        while right < len(s):
            arr[ord(s[right])] += 1
            right += 1
            while arr[ord(s[right - 1])] > 1:
                arr[ord(s[left])] -= 1
                left += 1
            res = max(res,right - left)
        return res
"""
主要是滑动窗口求到中间没有冗余字符，利用字符序列来求，本来可以用map但是字符数量少可以直接用数组代替
"""