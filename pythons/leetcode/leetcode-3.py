class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = [0] * 128
        n = len(s)
        ans = 0
        lef = rig = 0
        while rig < n:
            map[ord(s[rig])] += 1
            while map[ord(s[rig])] > 1 and lef <= rig:
                map[ord(s[lef])] -= 1
                lef += 1
            ans = max(ans,rig - lef + 1)
            rig += 1
        return ans