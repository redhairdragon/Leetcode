# https://leetcode.com/problems/permutations-ii/
from typing import List

class Solution:
    def permRec(self, letters,partial_res,res):
        if len(letters) == 0:
            res.append(partial_res)
            return

        visited = set()
        for i in range(len(letters)):
            if letters[i] not in visited:
                visited.add(letters[i])
                self.permRec(letters[0:i]+letters[i+1:], partial_res + [letters[i]],res)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return []
        self.permRec(nums,[],res)
        return res

# print(Solution().permuteUnique([1,1]))        
# print(Solution().permuteUnique([2,1,1]))        
# print(Solution().permuteUnique([2,1,1,2]))        
print(Solution().permuteUnique([3,3,0,3]))        

# print(Solution().permuteUnique([1]))        
# print(Solution().permuteUnique([]))        
# print(Solution().permuteUnique([1,2]))        
# print(Solution().permuteUnique([1,2,3]))        
# print(Solution().permuteUnique([1,2,3,4])) 