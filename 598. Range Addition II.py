# https://leetcode.com/problems/range-addition-ii/
from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return 0

        x = ops[0][0]
        y = ops[0][1]
        for coord in ops:
            x = min(x,coord[0])
            y = min(y,coord[1])

        return (x)*(y) 