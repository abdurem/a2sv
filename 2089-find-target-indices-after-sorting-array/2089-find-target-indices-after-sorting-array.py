import numpy as np
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        index=[]
        count=0
        for i in nums:
            if(i == target):
                index.append(count)
            count+=1
        return index
            
            