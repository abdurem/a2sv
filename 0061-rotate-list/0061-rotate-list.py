# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        cur=head
        ptr=[]
        i=0
        ptr.append(cur)
        while cur.next != None:
            ptr.append(cur.next)
            cur=cur.next
        
        k %= len(ptr)
        for i in range(k):
            ptr[-1].next = head
            ptr[-2].next = None
            head = ptr[-1]
            ptr.pop()
        return head