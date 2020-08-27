# https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x , next = None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node_idx_mapping=set()
        walker = head
        while walker != None:
            if walker in node_idx_mapping:
                return walker
            else:
                node_idx_mapping.add(walker)
                walker = walker.next

        return None
            

h1 = ListNode(0)
assert(Solution().detectCycle(h1) == None)
h2 = ListNode(0,ListNode(1,None))
assert(Solution().detectCycle(h2) == None)
h4 = ListNode(1)
h5 = ListNode(2,h4)
h6 = ListNode(3,h5)
h7 = ListNode(4,h6)
assert(Solution().detectCycle(h7) == None)
h8 = ListNode(1)
h9 = ListNode(2)
h10 = ListNode(3,h9)
h11 = ListNode(4,h10)
h9.next=h11
assert(Solution().detectCycle(h11) == h11)