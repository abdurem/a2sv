# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def findCycle(self,head):
        t=r=head
        
        while r:
            i=0
            while r and i < 2:
                r=r.next
                i+=1
            t=t.next
            if t == r:
                return r
        
        return None
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t,r=head,self.findCycle(head)
        if not r:
            return r
        
        while r!=t:
            r=r.next
            t=t.next
        return r