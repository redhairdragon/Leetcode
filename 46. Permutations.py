# https://leetcode.com/problems/permutations/
from typing import List

class Solution:
    def permRec(self, letters,partial_res,res):
        if len(letters) == 0:
            res.append(partial_res)
            return
        for i in range(len(letters)):
            self.permRec(letters[0:i]+letters[i+1:], partial_res + [letters[i]],res)


    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return []
        self.permRec(nums,[],res)
        return res

print(Solution().permute([1]))        
print(Solution().permute([]))        
print(Solution().permute([1,2]))        
print(Solution().permute([1,2,3]))        
print(Solution().permute([1,2,3,4]))        
