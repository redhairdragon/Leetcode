# https://leetcode.com/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        start = 0
        remain = 0 
        for i in range(len(gas)):
            if gas[i] + remain < cost[i]:
                start = i + 1
                remain = 0 
            else:
                remain += (gas[i] - cost[i])
        return start 

print(Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
        

