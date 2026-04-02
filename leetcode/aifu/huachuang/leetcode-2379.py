class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        cnt = 0
        for i, x in enumerate(blocks):
            if x == 'W':
                cnt += 1
            if i >= k - 1:
                ans = min(ans, cnt)
                if blocks[i - k + 1] == 'W':
                    cnt -= 1
        return ans


if __name__ == "__main__":
    print(Solution().minimumRecolors(blocks = "BWWWBB", k = 6))
