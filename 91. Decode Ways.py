# https://leetcode.com/problems/decode-ways/
class Solution:
    def isValid(self,s):
        if int(s) > 0 and int(s)<=26:
            return True
        return False

    def numDecodings(self, s: str) -> int:
        if s == "":
            return 0
        if len(s)==1:
            return 1 if self.isValid(s) else 0
        
        memory = [0]*(len(s)+1)

        if self.isValid(s[0]):
            memory [0] = 1
            memory [-1] = 1
        else:
            return 0
        # print(memory)

        for i in range(1,len(s)):
            if s[i]=="0":
                if not self.isValid(s[i-1:i+1]):
                    return 0
                memory[i] = 0
            else:    
                memory[i] = memory[i-1]
            
            if self.isValid(s[i-1:i+1]):
                if s[i-1] == "0":
                    memory[i]=memory[i-2]
                else:
                    memory[i]+=memory[i-2]

        
        return memory[-2]


assert(Solution().numDecodings("")==0)
assert(Solution().numDecodings("0")==0)
assert(Solution().numDecodings("1")==1)
assert(Solution().numDecodings("12")==2)
assert(Solution().numDecodings("19")==2)
assert(Solution().numDecodings("191")==2)
assert(Solution().numDecodings("226")==3)
assert(Solution().numDecodings("2266")==3)
assert(Solution().numDecodings("22623")==6)
assert(Solution().numDecodings("10")==1)
assert(Solution().numDecodings("101")==1)
assert(Solution().numDecodings("1011")==2)
assert(Solution().numDecodings("1000")==0)
assert(Solution().numDecodings("10110")==1)
assert(Solution().numDecodings("301")==0)
