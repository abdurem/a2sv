# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False
        
        t=r=head
        
        while r:
            i=0
            while r and i < 2:
                r=r.next
                i+=1
            t=t.next
            if t == r:
                return True
        
        return False