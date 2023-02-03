# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, k):
        cur=head.next
        prev=None
        tail=None
        for i in range(k):
            head.next=prev
            prev=head
            head=cur
            if not cur:
                break
            cur=cur.next
        return [prev,head]
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        cur=head
        size=0
        while cur != None:
            size+=1
            cur=cur.next
        
        cur=head
        count=0
        new,old = self.reverse(cur,k)
        count+=k
        prev=cur
        cur=old
        while count+k <= size:
            tmp,old = self.reverse(old,k)
            t=tmp
            while t.next:
                t=t.next
            prev.next = tmp
            prev=t
            cur = old
            count+=k
        prev.next = old
        return new