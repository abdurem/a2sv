# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self,head):
        count=0
        while head.next:
            count+=1
            head=head.next
        return [count,head]
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1,t1=self.count(l1)
        c2,t2=self.count(l2)
        
        for _ in range(c1,c2):
            node=ListNode()
            t1.next=node
            t1=node
        for _ in range(c2,c1):
            node=ListNode()
            t2.next=node
            t2=node
        c1=l1
        c2=l2
        rem=0
        ans=ListNode()
        tmp=ans
        while c1:
            node=ListNode()
            if c1.val+c2.val+rem > 9:
                node.val= (c1.val+c2.val+rem)%10
                tmp.next=node
                tmp=node
                rem=(c1.val+c2.val+rem)//10
            else:
                node.val= (c1.val+c2.val+rem)
                rem=0
                tmp.next=node
                tmp=node
            c1=c1.next
            c2=c2.next
        if rem:
            tmp.next=ListNode(rem)
        return ans.next
