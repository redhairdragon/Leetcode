# https://leetcode.com/problems/binary-subarrays-with-sum/
from typing import List

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        prefix_sum = [0]
        memory = {0:1}
        for i in A:
            prefix_sum.append(prefix_sum[-1]+i)
            
        res = 0

        prefix_sum=prefix_sum[1:]
        for i in prefix_sum:
            print(memory)
            if i - S in memory:
                res += memory[i-S]
            if i in memory:
                memory[i] += 1
            else:
                memory[i] = 1
        
        return res

# print(Solution().numSubarraysWithSum([1,0,1,0,1],1))
# print(Solution().numSubarraysWithSum([0,0,0,0,0],0))
# print(Solution().numSubarraysWithSum([0,0,0,0,0,0,1,0,0,0],0))

