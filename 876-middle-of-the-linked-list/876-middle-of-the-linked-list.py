# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        j=head
        i=head
        c=0
        
        while i.next != None:
            i=i.next
            c+=1
            if i.next != None:
                i=i.next
                c+=1
            j=j.next
        
        
        return j