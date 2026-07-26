class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        se = set(['a', 'e', 'i', 'o', 'u'])
        ans = 0
        count = 0
        for i in range(len(s)):
            if s[i] in se:
                count += 1
            if i >= k and s[i - k] in se:
                count -= 1
            if i > k - 1:
                ans = max(ans, count)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxVowels(s="weallloveyou", k=7))
