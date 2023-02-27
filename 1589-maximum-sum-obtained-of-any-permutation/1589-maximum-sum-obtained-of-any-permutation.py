class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        '''
        approach
        
        create an array of zeros to hold the prefix sum with length of nums plus 1.
        add the queries in request and adjust the prefix sum array to the conditions.
        calculate the prefix sum of the array and sort it.
        initialize an answer variable to zero and add the product of the prefix sum to the number array.
        return answer
        '''
        preSum=[0]*(len(nums)+1)
        
        for l,r in requests:
            preSum[l]+=1
            preSum[r+1]-=1
        preSum=list(accumulate(i for i in preSum[:-1]))
        preSum.sort()
        nums.sort()
        ans=0
        
        for i in range(len(nums)-1,-1,-1):
            ans+=(preSum[i]*nums[i])
        return ans%((10**9)+7)