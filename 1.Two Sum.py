# https://leetcode.com/problems/two-sum/
# Save to dictionary mapping Easy:)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number2index = {}
        for index,number in enumerate(nums):
            diff = target - number
            if diff in number2index:
                return [number2index[diff],index]
            number2index[number] = index

print(Solution().twoSum([2,2,3,4,8,5,0],5))
print(Solution().twoSum([3,0,4],4))
print(Solution().twoSum([-5,0,3],2))
