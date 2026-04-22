import sys
input = sys.stdin.readline

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [''] * numRows
        if numRows == 1:
            return s
        i = 0
        flag = 1
        j = 0
        while j < len(s):
            ans[i] = ans[i] + s[j]
            if i == numRows - 1:
                flag = -1
            elif i == 0:
                flag = 1
            i += flag
            j += 1
        return ''.join(ans)
if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))