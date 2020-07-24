# https://leetcode.com/problems/container-with-most-water/
from typing import List


def getArea(i,j,h):
    return min(h[i],h[j])*(j-i)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxAreaNow = 0
        left = 0
        right = len(height) - 1
        while left != right:
            maxAreaNow = max(maxAreaNow, getArea(left,right,height))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxAreaNow

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
