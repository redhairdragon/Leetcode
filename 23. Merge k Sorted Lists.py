# https://leetcode.com/problems/merge-k-sorted-lists//
from typing import List
from queue import PriorityQueue

#这题注意tuple的比较原理
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = PriorityQueue()
        
        head = point = ListNode(0)
        index = 0
        for l in lists:
            if l:
                q.put((l.val, index,l))
            index+=1

        while not q.empty():
            val,index, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, index, node))
        return head.next