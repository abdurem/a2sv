# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head:
            return None
        if not head.next:
            return head
        
        dum = ListNode()
        dum.next=head
        
        prv=dum
        pos=None
        while prv.next != None and prv.next.val != x:
            if prv.next.val >= x:
                break
            prv=prv.next
            
        ptr=prv
        cur=prv.next
        prev=cur
        
        while cur != None:
            if cur.val < x:
                prev.next = cur.next
                cur.next = ptr.next
                ptr.next = cur
                cur=prev
                ptr=ptr.next
                continue
            prev=cur
            cur=cur.next
        
        return dum.next
                
        
        
        
        