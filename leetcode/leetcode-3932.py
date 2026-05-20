class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return r - l + 1
        lef = int(l ** (1 / k))
        rig = int(r ** (1 / k)) + 1
        ans = 0
        for i in range(int(lef), int(rig) + 2):
            if i ** k >= l and i ** k <= r:
                ans += 1
        return ans
if __name__=='__main__':
    l = 30
    r = 64
    k = 3
    print(Solution().countKthRoots(l, r, k))