# https://leetcode.com/problems/edit-distance/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memory = dict()

        def rec(w1,w2,i,j):
            if (len(w1)==0):
                return len(w2)
            if (len(w2)==0):
                return len(w1)
            if (i,j) in memory:
                return memory[(i,j)]

            w1_=w1[1:]
            w2_=w2[1:]
            delete = 1 + rec(w1_,w2,i+1,j)
            replace = rec(w1_,w2_,i+1,j+1)
            if w1[0] != w2[0]:
                replace+=1
            add = 1 + rec(w1,w2_,i,j+1)

            memory[(i,j)]= min(min(replace, delete), add)
            return memory[(i,j)]

        return rec(word1,word2,0,0)    
  

print(Solution().minDistance( "horse","ros"))
assert(Solution().minDistance( "horse","ros")==3)