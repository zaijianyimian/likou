import collections
from typing import List

# 207 课程表 拓扑排序解决
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for x,y in prerequisites:
            graph[x].append(y) # 链式存储
            indegree[y] += 1
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        completed = 0
        while queue:
            node = queue.popleft()
            completed += 1
            for nex in graph[node]:
                indegree[nex] -= 1
                if indegree[nex] == 0:
                    queue.append(nex)
        return completed == numCourses

