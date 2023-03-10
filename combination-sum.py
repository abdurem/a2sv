class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]

        def backtrack(start, comb):
            if sum(comb) == target:
                ans.append(comb[:])
                return
            
            if sum(comb) > target:
                return
            # print(sum(comb))
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb)
                comb.pop()
                
        backtrack(0,[])
        return ans