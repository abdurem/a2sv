# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        if not head.next or not head.next.next:
            return head
        
        tail=head
        
        while tail.next:
            tail=tail.next
        
        odd=head
        even=tail
        eHead=head.next
        
        while odd != eHead and odd.next != eHead or head.next == eHead:
            tmp=odd.next
            odd.next=tmp.next
            even.next=tmp
            tmp.next=None
            odd=odd.next
            even=tmp

        return head
        