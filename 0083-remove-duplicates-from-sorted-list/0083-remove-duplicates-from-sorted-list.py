# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        elif head.next == None:
            return head
        
        else:
            cur = head
            nxt = head.next
            
            while cur.next != None:
                if cur.val != nxt.val:
                    cur = cur.next
                else:
                    cur.next = nxt.next
                nxt = nxt.next
            return head
            