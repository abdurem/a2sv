# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1,cur2=list1,list2
        ans=ListNode()
        tmp=ans
        while cur1 and cur2:
            if cur1.val < cur2.val:
                tmp.next=ListNode(cur1.val)
                cur1=cur1.next
            else:
                tmp.next=ListNode(cur2.val)
                cur2=cur2.next
            tmp=tmp.next
        if cur1:
            tmp.next=cur1
        elif cur2:
            tmp.next=cur2
        return ans.next