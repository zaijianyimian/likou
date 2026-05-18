import collections
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        if arr[start] == 0:
            return True
        visited = [False] * n
        queue = collections.deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            nextNode = node + arr[node]
            preNode = node - arr[node]
            if nextNode < n and not visited[nextNode]:
                queue.append(nextNode)
                if arr[nextNode] == 0:
                    return True
                visited[nextNode] = True
            if preNode >= 0 and not visited[preNode]:
                queue.append(preNode)
                if arr[preNode] == 0:
                    return True
                visited[preNode] = True

        return False
if __name__ == '__main__':
    s = Solution()
    print(s.canReach([3,0,2,1,2], 2))