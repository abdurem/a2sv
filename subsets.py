class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start, arr):
            flag = (arr in ans)
            if flag:
                return
            
            if not flag:
                ans.append(arr[:])
            
            for i in range(start, len(nums)):
                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()
            

        backtrack(0, [])
        return ans