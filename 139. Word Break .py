# https://leetcode.com/problems/word-break/
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True
        if len(wordDict) == 0:
            return False
        
        memory = [False] * (len(s) + 1)
        memory[-1] = True
        for i in range(len(s)):
            # print(memory)
            for w in wordDict:
                if i + 1 - len(w) >= 0:
                    # print(s[i + 1 - len(w):i+1] )
                    if s[i + 1 - len(w):i+1] == w:
                        memory[i] = True and memory[i - len(w)]
                        if memory[i] == True:
                            break
        # print(memory)
        
        return memory[-2]


        

assert(Solution().wordBreak(s = "leetcode", wordDict = ["leet", "code"])==True)
assert(Solution().wordBreak(s = "codeleet", wordDict = ["leet", "code"])==True)
assert(Solution().wordBreak(s = "leetcod", wordDict = ["leet", "code"])==False)
assert(Solution().wordBreak(s = "leece", wordDict = ["leet", "code"])==False)
assert(Solution().wordBreak(s = "leece", wordDict = [])==False)
assert(Solution().wordBreak(s = "gobruin", wordDict = ["g","obruin"])==True)
assert(Solution().wordBreak(s = "gobruin", wordDict = ["g","go","bruin","obruin"])==True)
assert(Solution().wordBreak(s = "gobruin", wordDict = ["g","obruin"])==True)
assert(Solution().wordBreak(s = "g", wordDict = ["g","obruin"])==True)
assert(Solution().wordBreak(s = "g", wordDict = ["z"])==False)
assert(Solution().wordBreak(s = "", wordDict = ["z"])==True)
assert(Solution().wordBreak(s = "", wordDict = [])==True)

assert(Solution().wordBreak(s = "dogs", wordDict = ["dog","s","gs"])==True)



