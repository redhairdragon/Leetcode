# Definition for singly-linked list.
class ListNode:
    def __init__(self, x , next):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        if slow == None: #This is the edge case worth noting
            return False

        fast = slow.next
        while slow:
            if slow == fast:
                return True
            if fast == None:
                return False
            if fast.next == None:
                return False

            slow = slow.next
            fast = fast.next.next

n0=ListNode(0,None)
n1=ListNode(1,n0)
n2=ListNode(1,n1)
n3=ListNode(5,n2)
n4=ListNode(4,n3)
n5=ListNode(2,n4)

n1.next=n5
print(Solution().hasCycle(n5))        

