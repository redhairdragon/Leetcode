# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:  return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1

        # find index of the smallest 
        left = 0
        right = len(nums) - 1 

        while(left < right):
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
       
        pivot = left
        minimum = nums[pivot]

        left = 0
        right = len(nums) - 1
        if target >= nums[0]:
            right = (pivot - 1)%len(nums) 
        else:
            left = pivot
            right = len(nums) - 1
        
        # print("Pivot " + str(pivot))
        while left <= right:
            mid = (left + right)//2
            # print("left  " + str(left))
            # print("right " + str(right))
            # print("mid   " + str(mid))

            if left == right:
                if nums[mid]!=target:
                    return -1

            if nums[mid] == target:
                return mid 
            if target > nums[mid]:
                left = mid + 1
            else: 
                right = mid
        return -1


assert(Solution().search([4,5,6,7,0,1,2],0) == 4)
assert(Solution().search([2],0) == -1)
assert(Solution().search([],2) == -1)
assert(Solution().search([2],2) == 0)
assert(Solution().search([4,5,6,7,0,1,2],3) == -1)
assert(Solution().search([4,5,6,7,0,1,2,3],1) == 5)
assert(Solution().search([4,5,6,7,0,1,2,3],3) == 7)
assert(Solution().search([0,1,2,3],3) == 3)
assert(Solution().search([0,1,2,3],4) == -1)
assert(Solution().search([1,3],0) == -1)
assert(Solution().search([3,1],3) == 0)
