# https://leetcode.com/problems/subarray-sums-divisible-by-k/
from typing import List
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix_sum = 0
        result = 0
        partial_result = [1] + [0]*(K-1)
        for i in A:
            prefix_sum = (prefix_sum+i) % K
            result += partial_result[ prefix_sum ]
            partial_result[prefix_sum]+=1
        return result
                
        

print(Solution().subarraysDivByK([4,5,0,-2,-3,1],5))
print(Solution().subarraysDivByK([0,0],5))
print(Solution().subarraysDivByK([1,1],1))