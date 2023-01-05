class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        sum_ = sum(num for num in nums if num%2 == 0)
        ans=[]
        
        for q,i in queries:
            if nums[i]%2 == 0:
                sum_-=nums[i]
            nums[i]+=q
            if nums[i]%2 == 0:
                sum_+=nums[i]
            ans.append(sum_)
        return ans