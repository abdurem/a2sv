# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        for i in range(1,len(lists)):
            c1=ListNode()
            c1.next=lists[0]
            head=c1
            c2=lists[i]
            
            while c1.next!=None and c2:
                if c1.next.val > c2.val:
                    tmp=c2
                    c2=c2.next
                    tmp.next=c1.next
                    c1.next=tmp
                else:
                    c1=c1.next
            if c2:
                c1.next=c2
            
            lists[0]=head.next
        return lists[0]
                