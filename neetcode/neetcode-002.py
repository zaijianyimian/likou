class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr =[0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        for c in t:
            tmp = ord(c) - ord('a')
            arr[tmp] -= 1
            if arr[tmp] < 0:
                return False
        return True