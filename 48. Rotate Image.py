# https://leetcode.com/problems/rotate-image/
from typing import List
class Solution:
    def rotate_coord(self,x,y,mat):
        n = len(mat)
        if x >= n//2:
            return
        if x >= y:
            return
        if y >= n - x:
            return
        
        tmp0=mat[x][y]
        tmp1=mat[y][n-1-x]
        tmp2=mat[n-1-x][n-1-y]
        tmp3=mat[n-1-y][x]
        mat[x][y]=tmp3
        mat[y][n-1-x]=tmp0
        mat[n-1-x][n-1-y]=tmp1
        mat[n-1-y][x]=tmp2



    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                self.rotate_coord(i,j,matrix)

        
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b=[[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(a)
print(a)
Solution().rotate(b)
print(b)