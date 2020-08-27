# https://leetcode.com/problems/number-of-islands/
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        row = len(grid)
        col = len(grid[0])

        visited= [[False for i in range(col)] for j in range(row)]

        def dfs(i,j):
            if i < 0 or i >= row or j < 0 or j >= col:
                return
            if grid[i][j] == "0":
                return 
            if not visited[i][j]:
                visited[i][j] = True
                # print(visited)
                dfs(i,j-1)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i+1,j)

        res = 0
        for i in range(row):
            for j in range(col):
                # print(visited)
                if not visited[i][j] and grid[i][j] == "1":
                    # print("in for loop: "+ str((i,j)))
                    res += 1
                    dfs(i,j)
                # print("res: " + str(res))
        return res

grid =  [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
assert(Solution().numIslands(grid) == 1)
        
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
assert(Solution().numIslands(grid) == 3)

grid = [["0","1","0"],
        ["1","0","1"],
        ["0","1","0"]]
assert(Solution().numIslands(grid) == 4)
