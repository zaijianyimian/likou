import collections
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        graph = collections.defaultdict(list)
        for i in range(n):
            graph[arr[i]].append(i)
        queue = collections.deque([0])
        visited = [False] * n
        step = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == n - 1:
                    return step
                neighbors = []
                if node + 1 < n:
                    neighbors.append(node + 1)
                if node - 1 >= 0:
                    neighbors.append(node - 1)
                neighbors.extend(graph[arr[node]])
                # 将所有另据都加入neighbors中
                for j in neighbors:
                    if not visited[j]:
                        visited[j] = True
                        queue.append(j)
                graph[arr[node]].clear()
            # 每次bfs完成后
            step += 1
        return -1
if __name__ == '__main__':
    s = Solution()
    print(s.minJumps([100,-23,-23,404,100,23,23,23,3,404]))