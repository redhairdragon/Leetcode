# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]

        memory = [0]*(len(cost)+2)
        for i in range(len(cost)):
            memory[i] = cost[i]+ min(memory[i-1], memory[i-2])
            # print(memory)
        return min(memory[-3],memory[-4])

assert(Solution().minCostClimbingStairs( [ ])==0)
assert(Solution().minCostClimbingStairs( [10, 15, 20])==15)
assert(Solution().minCostClimbingStairs( [1, 100, 1, 1, 1, 100, 1, 1, 100, 1])==6)