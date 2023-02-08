# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        fast=slow=head
        while fast.next:
            count+=1
            i=0
            while fast.next and i < 2:
                i+=1
                fast=fast.next
            slow=slow.next
        
        return slow