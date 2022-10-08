class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        right=[1]*len(nums)
        ans=[]
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
            right[len(nums)-i-1] = right[len(nums)-i]*nums[len(nums)-i]
        for i in range(len(nums)):
            ans.append(left[i]*right[i])
        return ans
        
        
        