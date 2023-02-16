# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        n = len(values)
        ans = [0] * n

        stack = []

        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= values[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(values[i])

        return ans