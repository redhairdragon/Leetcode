# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set_mapping = dict()
        for n in nums:
            if n in num_set_mapping:
                continue
            if n - 1 in num_set_mapping and n + 1 not in num_set_mapping:
                num_set_mapping[n] = num_set_mapping[n - 1] 
            elif n - 1 not in num_set_mapping and n + 1 in num_set_mapping:
                num_set_mapping[n] = num_set_mapping[n + 1]
            elif n - 1 in num_set_mapping and n + 1 in num_set_mapping:
                num_set_mapping[n] = num_set_mapping[n - 1].union(num_set_mapping[n + 1])
                for x in num_set_mapping[n]:
                    num_set_mapping[x] = num_set_mapping[n]
            else:
                num_set_mapping[n] = set()
            num_set_mapping[n].add(n)

        res = 0
        for s in num_set_mapping.values():
            res = max(res,len(s))
        return res


assert(Solution().longestConsecutive([])==0)
assert(Solution().longestConsecutive([100, 4, 200, 1, 3, 2])==4)
assert(Solution().longestConsecutive([100, 4, 200, 11, 10, 2])==2)
assert(Solution().longestConsecutive([100])==1)
assert(Solution().longestConsecutive([1,3,5,2,4])==5)
assert(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])==9)
