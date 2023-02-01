# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ptrs=[]
        cur = head
        while cur.next != None:
            ptrs.append(cur.next)
            cur = cur.next
        ptrs = [head]+ptrs
        
        l=0
        r=len(ptrs)-1
        while l < r:
            if ptrs[l].val != ptrs[r].val:
                return False
            l+=1
            r-=1
        return True