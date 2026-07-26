class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []
        path = []
        def dfs(index : int,cost: int) -> None:
            if index == n:
                ans.append("".join(path))
                return
            path.append('0')
            dfs(index+1,cost)
            path.pop()
            if(not path or path[-1] != '1') and cost + index <= k:
                path.append('1')
                dfs(index + 1,cost + index)
                path.pop()
        dfs(0,0)
        return ans