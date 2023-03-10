# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        fast=slow=prev=head
        while fast and fast.next:
            prev=slow
            fast = fast.next.next
            slow=slow.next
        
        prev.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(slow)
        merged = self.concur(h1, h2)

        return merged        

    def concur(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1

        merged = ListNode()
        if head1.val < head2.val:
            head1.next = self.concur(head1.next, head2)
            merged = head1

        else:
            head2.next = self.concur(head1, head2.next)
            merged = head2

        return merged