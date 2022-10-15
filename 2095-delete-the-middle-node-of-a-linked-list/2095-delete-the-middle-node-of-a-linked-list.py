# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        slow,fast=head,head 
        c=2

        while fast.next:
            if c == 0:
                slow=slow.next
                c=2
            fast=fast.next
            c-=1
        slow.next=slow.next.next
        return head
