from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        prefix = [0]* len(gas)
        mi = float('inf')
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            if i == 0:
                prefix[i] = diff
            else:
                prefix[i] = prefix[i - 1] + diff
            if prefix[i] < mi:
                mi = prefix[i]
                start = (i + 1) % len(gas)
        return start if prefix[-1] >= 0 else -1

