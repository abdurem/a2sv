# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode(0,next=head)
        Sorted=head
        cur=head.next
        search=ans
        
        while cur:
            search=ans.next
            if cur.val < Sorted.val:
                prev=ans
                while search.val < cur.val and search != Sorted:
                    prev=search
                    search = search.next
                Sorted.next=cur.next
                cur.next=search
                prev.next=cur
                cur=Sorted.next
            else:
                Sorted=Sorted.next
                cur=cur.next
        return ans.next
                