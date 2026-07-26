import sys
input = sys.stdin.readline

class Solution:
    def mirrorDistance(self, n: int) -> int:
        m = reversed(str(n))
        m = int(''.join(m))
        return abs(n-m)
if __name__=="__main__":
    n = int(input())
    s = Solution()
    print(s.mirrorDistance(n))