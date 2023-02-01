# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        ptr=[]
        cur=head
        ptr.append(cur)
        while cur.next != None:
            ptr.append(cur.next)
            cur = cur.next
        if n+1 > len(ptr):
            head=head.next
        else:
            ptr[(-1*n)-1].next = ptr[-1*n].next
        return head