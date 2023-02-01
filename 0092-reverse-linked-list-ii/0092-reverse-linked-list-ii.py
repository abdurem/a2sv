# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lft = rgt = head
        
        for _ in range(left-1):
            lft = lft.next
            
        for _ in range(right-1):
            rgt = rgt.next
        
        ptrs = []
        cur=lft
        for i in range(left+1,right):
            ptrs.append(cur.next)
            cur = cur.next
        ptrs.insert(0,lft)
        ptrs.append(rgt)
        
        lft=0
        rgt=len(ptrs)-1
        while lft < rgt:
            ptrs[lft].val,ptrs[rgt].val = ptrs[rgt].val,ptrs[lft].val
            lft+=1
            rgt-=1
        return head