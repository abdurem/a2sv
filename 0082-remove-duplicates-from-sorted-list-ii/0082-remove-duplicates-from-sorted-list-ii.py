# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        elif not head.next:
            return head
        cur=head
        nxt=cur.next
        prev=ListNode()
        prev.next = cur
        ans=prev
        
        while cur.next:
            if cur.val == nxt.val:
                while nxt and cur.val == nxt.val:
                    nxt = nxt.next
                prev.next = nxt
                cur=nxt
                if not nxt:
                    break
                nxt=nxt.next
                continue
            prev=prev.next
            cur=cur.next
            nxt=nxt.next

        return ans.next
            
            