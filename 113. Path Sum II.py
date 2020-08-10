# Definition for a binary tree node.
# https://leetcode.com/problems/path-sum-ii/
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSumRec(self, root, currLst, s, res):
        if root == None:
            return

        s = s - root.val

        if root.left==None and root.right==None:
            if s == 0:
                res.append(currLst+[root.val])
        
        self.pathSumRec(root.left, currLst+[root.val], s,res)
        self.pathSumRec(root.right, currLst+[root.val], s,res)



    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        self.pathSumRec(root,[],sum,result)
        return result

# Test case 1
# root = TreeNode(1)
# print(Solution().pathSum(root,1))
# print(Solution().pathSum(root,0))



root1 = TreeNode(1,TreeNode(2))
# print(Solution().pathSum(root1,0))
# print(Solution().pathSum(root1,1))
# print(Solution().pathSum(root1,2))
# print(Solution().pathSum(root1,3))

root2 = TreeNode(1,TreeNode(2),TreeNode(3))
# print(Solution().pathSum(root2,0))
# print(Solution().pathSum(root2,1))
# print(Solution().pathSum(root2,2))
# print(Solution().pathSum(root2,3))
# print(Solution().pathSum(root2,4))

root3 = TreeNode(1,TreeNode(2,TreeNode(5)),TreeNode(3))
# print(Solution().pathSum(root3,0))
# print(Solution().pathSum(root3,4))
# print(Solution().pathSum(root3,8))

root4 = TreeNode(1,TreeNode(2,TreeNode(5),TreeNode(3,None,TreeNode(2))),TreeNode(3,None,TreeNode(2)))
print(Solution().pathSum(root4,8))


