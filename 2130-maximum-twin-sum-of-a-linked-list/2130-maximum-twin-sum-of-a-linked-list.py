# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        if not head.next.next:
            return head.val+head.next.val
        
        s=f=head
        tail=None
        while f and f.next:
            tail=f
            f=f.next.next
            if not f:
                break
            s=s.next
        
        cur=s.next
        s.next=None
        prev=None
        while cur.next:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        cur.next=prev
        
        f=head
        b=cur
        ans=0
        while f and b:
            ans=max(ans,f.val+b.val)
            f=f.next
            b=b.next
        return ans