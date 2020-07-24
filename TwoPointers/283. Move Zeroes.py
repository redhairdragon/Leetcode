# https://leetcode.com/problems/move-zeroes/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        traverser = 0  
        updater = 0
        while traverser != len(nums):
            if nums[traverser] == 0:
                traverser+=1
            elif nums[traverser] != 0:
                nums[updater] = nums[traverser]
                traverser+=1
                updater+=1
        
        while updater != traverser:
            nums[updater] = 0
            updater += 1 

nums = [0,2,1]
Solution().moveZeroes(nums)
print(nums)