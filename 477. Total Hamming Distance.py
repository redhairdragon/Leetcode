# https://leetcode.com/problems/total-hamming-distance/
from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        binaries = list(map(lambda x: bin(x)))