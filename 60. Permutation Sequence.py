# https://leetcode.com/problems/permutation-sequence/
import math

class Solution:
    
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1,n+1)]

        def rec(rest,cnt):
            if len(rest) == 1:
                return str(rest[0])
            # print(rest)
            for i in range(len(rest)):
                # print(cnt)
                if cnt - math.factorial(len(rest)-1) <= 0:
                    return str(rest[i]) + rec(rest[0:i]+rest[i+1:],cnt )
                else:
                    cnt-= math.factorial(len(rest)-1)
        return rec(nums,k)

# print((Solution().getPermutation(1,1)))
# print(Solution().getPermutation(3,3))
# print(Solution().getPermutation(4,9))