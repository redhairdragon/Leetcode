# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List

class Solution:
    def rec(self, digits, curr,res,tel):
        if len(digits)==0:
            res.append(curr)
            return 
        currDigit = digits[0]
        for l in tel[currDigit]:
            self.rec(digits[1:],curr+l, res,tel)
        

    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        tel=dict()
        tel["2"]="abc"
        tel["3"]="def"
        tel["4"]="ghi"
        tel["5"]="jkl"
        tel["6"]="mno"
        tel["7"]="pqrs"
        tel["8"]="tuv"
        tel["9"]="wxyz"
        result=[]
        self.rec(digits,"",result,tel)
        return result

print(Solution().letterCombinations("23"))        
print(Solution().letterCombinations("234"))        