# https://leetcode.com/problems/sort-colors/
from typing import List

#Something like three pointer
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
    
        walker = 0
        while walker != len(nums):
            if nums[walker] == 0:
                red += 1
                white += 1
            if nums[walker] == 1:
                white += 1
            walker+=1

        for i in range(red):
            nums[i] = 0
        for i in range(red,white):
            nums[i] = 1
        for i in range(white,len(nums)):
            nums[i] = 2

n = [2,1 ,2]
Solution().sortColors(n)
print(n)     
