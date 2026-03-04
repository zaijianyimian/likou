from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1,len(s) + 1):
            for w in wordDict:
                if len(w)<= i:
                    if s[i - len(w):i] == w:
                        dp[i] = max(dp[i],dp[i - len(w)])
        return dp[-1] == 1