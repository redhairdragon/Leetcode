# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSumRec(self, root, partialSum, s):
        if root == None:
            return False

        newSum = partialSum+root.val

        if root.left==None and root.right==None:
            if newSum == s:
                return True
            return False
        
        return self.hasPathSumRec(root.left, newSum, s) or self.hasPathSumRec(root.right, newSum, s)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.hasPathSumRec(root,0,sum)

# Test case 1
root = TreeNode(1)
print(Solution().hasPathSum(root,1))
print(Solution().hasPathSum(root,0))



root1 = TreeNode(1,TreeNode(2))
print(Solution().hasPathSum(root1,0))
print(Solution().hasPathSum(root1,1))
print(Solution().hasPathSum(root1,2))
print(Solution().hasPathSum(root1,3))

root2 = TreeNode(1,TreeNode(2),TreeNode(3))
print(Solution().hasPathSum(root2,0))
print(Solution().hasPathSum(root2,1))
print(Solution().hasPathSum(root2,2))
print(Solution().hasPathSum(root2,3))
print(Solution().hasPathSum(root2,4))

root3 = TreeNode(1,TreeNode(2,TreeNode(5)),TreeNode(3))
print(Solution().hasPathSum(root3,0))
print(Solution().hasPathSum(root3,4))
print(Solution().hasPathSum(root3,8))
