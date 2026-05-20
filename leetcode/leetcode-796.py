class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        tmp = goal + goal
        return s in tmp and len(s) == len(goal)