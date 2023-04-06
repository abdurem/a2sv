class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(arr, flag, ans):
            if all(flag):
                ans.append(arr[:])
                return
            
            for i in range(len(nums)):
                if not flag[i]:
                    flag[i]=True
                    arr.append(nums[i])
                    backtrack(arr,flag,ans)
                    arr.pop()
                    flag[i] = False
        
        flag  = [False] * len(nums)
        backtrack([], flag, ans)
        return ans