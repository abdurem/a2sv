# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head.next
        if not cur:
            return head
        
        while cur.next != None:
            cur=cur.next
        tail = cur
        cur=head
        
        while cur != tail:
            tmp = cur.next
            cur.next = tail.next
            tail.next = cur
            cur = tmp
        return cur
        