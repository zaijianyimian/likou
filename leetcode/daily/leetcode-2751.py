from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        ids = sorted(range(len(positions)),key=lambda x:positions[x])
        for i in ids:
            if directions[i] == "R":
                stack.append(i)
                continue
            while stack:
                j = stack[-1]
                if healths[j] > healths[i]:
                    healths[j] -= 1
                    healths[i] = 0
                    break
                elif healths[j] == healths[i]:
                    healths[j] = 0
                    healths[i] = 0
                    stack.pop()
                    break
                else:
                    healths[i] -= 1
                    healths[j] = 0
                    stack.pop()
        return [h for h in healths if h > 0]

