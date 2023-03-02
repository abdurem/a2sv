class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        rear=1
        n=len(nums)
        ans=[-1]*n
        
        for front in range(n):
            rear=(front+1)%n
            while rear != front:
                if nums[front] < nums[rear]:
                    ans[front]=nums[rear]
                    break
                rear = (rear+1)%n
        return ans
            