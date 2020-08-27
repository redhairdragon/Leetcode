# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate(x):
            squared_sum = 0
            while (x != 0):
                squared_sum += (x%10)**2
                x = x //10
            return squared_sum
        
        memory =set()
        memory.add(n)
        while n != 1:
            n = calculate(n)
            if n in memory:
                return False
            memory.add(n)
        return True

assert(Solution().isHappy(19) == True)
assert(Solution().isHappy(1) == True)
assert(Solution().isHappy(0) == False)