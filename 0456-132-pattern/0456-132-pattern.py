class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        r=1
        mn=float(-inf)
        stk=[]
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < mn:
                return True
            
            while stk and stk[-1] < nums[i]:
                mn = stk.pop()
            stk.append(nums[i])
        return False