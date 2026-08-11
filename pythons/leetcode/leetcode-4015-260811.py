import collections


class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        dic = collections.defaultdict(list)
        for i in range(len(parent)):
            if i == 0:
                continue
            dic[parent[i]].append(i)
        def dfs() -> int:
            n = len(parent)
            depth = [0] * n
            depth[0] = 1
            queue = collections.deque([0])
            h = 1
            while queue:
                node = queue.popleft()
                for child in dic[node]:
                    depth[child] = depth[node] + 1
                    queue.append(child)
                    h = max(h, depth[child])

            return h,depth
        h,depth = dfs()
        ans = 0
        for i,x in enumerate(nums):
            ans += x * (h - depth[i] + 1)
        return ans
