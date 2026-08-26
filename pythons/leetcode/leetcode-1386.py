from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        dic = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                dic[row] |= 1 << (seat - 2)
        empty_row = n - len(dic)
        ans = empty_row * 2
        for x in dic.values():
            if x & 0b1111 == 0 or x & 0b111100 == 0 or x & 0b11110000 == 0:
                ans += 1
        return ans
