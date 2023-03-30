class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=set()

        def backtrack(idx, arr):
            if idx >= len(nums):
                if len(arr) > 1:
                    ans.add(tuple(arr))
                return
            
            if len(arr) > 1:
                ans.add(tuple(arr))
            
            for i in range(idx, len(nums)):
                if not arr or arr[-1] <= nums[i]:
                    arr.append(nums[i])
                    backtrack(i+1,arr)
                    arr.pop()
            
        backtrack(0,[])
        return ans